#include <assert.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#include "/home/5unKn0wn/ctfs/2018/*ctf/check.h"
#define UNLIKELY(x) __builtin_expect(!!(x), 0)
#define LIKELY(x) __builtin_expect(!!(x), 1)

#define TRAP(x) (wasm_rt_trap(WASM_RT_TRAP_##x), 0)

#define FUNC_PROLOGUE                                            \
  if (++wasm_rt_call_stack_depth > WASM_RT_MAX_CALL_STACK_DEPTH) \
    TRAP(EXHAUSTION)

#define FUNC_EPILOGUE --wasm_rt_call_stack_depth

#define UNREACHABLE TRAP(UNREACHABLE)

#define CALL_INDIRECT(table, t, ft, x, ...)          \
  (LIKELY((x) < table.size && table.data[x].func &&  \
          table.data[x].func_type == func_types[ft]) \
       ? ((t)table.data[x].func)(__VA_ARGS__)        \
       : TRAP(CALL_INDIRECT))

#define MEMCHECK(mem, a, t)  \
  if (UNLIKELY((a) + sizeof(t) > mem->size)) TRAP(OOB)

#define DEFINE_LOAD(name, t1, t2, t3)              \
  static inline t3 name(wasm_rt_memory_t* mem, u64 addr) {   \
    MEMCHECK(mem, addr, t1);                       \
    t1 result;                                     \
    memcpy(&result, &mem->data[addr], sizeof(t1)); \
    return (t3)(t2)result;                         \
  }

#define DEFINE_STORE(name, t1, t2)                           \
  static inline void name(wasm_rt_memory_t* mem, u64 addr, t2 value) { \
    MEMCHECK(mem, addr, t1);                                 \
    t1 wrapped = (t1)value;                                  \
    memcpy(&mem->data[addr], &wrapped, sizeof(t1));          \
  }

DEFINE_LOAD(i32_load, u32, u32, u32);
DEFINE_LOAD(i64_load, u64, u64, u64);
DEFINE_LOAD(f32_load, f32, f32, f32);
DEFINE_LOAD(f64_load, f64, f64, f64);
DEFINE_LOAD(i32_load8_s, s8, s32, u32);
DEFINE_LOAD(i64_load8_s, s8, s64, u64);
DEFINE_LOAD(i32_load8_u, u8, u32, u32);
DEFINE_LOAD(i64_load8_u, u8, u64, u64);
DEFINE_LOAD(i32_load16_s, s16, s32, u32);
DEFINE_LOAD(i64_load16_s, s16, s64, u64);
DEFINE_LOAD(i32_load16_u, u16, u32, u32);
DEFINE_LOAD(i64_load16_u, u16, u64, u64);
DEFINE_LOAD(i64_load32_s, s32, s64, u64);
DEFINE_LOAD(i64_load32_u, u32, u64, u64);
DEFINE_STORE(i32_store, u32, u32);
DEFINE_STORE(i64_store, u64, u64);
DEFINE_STORE(f32_store, f32, f32);
DEFINE_STORE(f64_store, f64, f64);
DEFINE_STORE(i32_store8, u8, u32);
DEFINE_STORE(i32_store16, u16, u32);
DEFINE_STORE(i64_store8, u8, u64);
DEFINE_STORE(i64_store16, u16, u64);
DEFINE_STORE(i64_store32, u32, u64);

#define I32_CLZ(x) ((x) ? __builtin_clz(x) : 32)
#define I64_CLZ(x) ((x) ? __builtin_clzll(x) : 64)
#define I32_CTZ(x) ((x) ? __builtin_ctz(x) : 32)
#define I64_CTZ(x) ((x) ? __builtin_ctzll(x) : 64)
#define I32_POPCNT(x) (__builtin_popcount(x))
#define I64_POPCNT(x) (__builtin_popcountll(x))

#define DIV_S(ut, min, x, y)                                 \
   ((UNLIKELY((y) == 0)) ?                TRAP(DIV_BY_ZERO)  \
  : (UNLIKELY((x) == min && (y) == -1)) ? TRAP(INT_OVERFLOW) \
  : (ut)((x) / (y)))

#define REM_S(ut, min, x, y)                                \
   ((UNLIKELY((y) == 0)) ?                TRAP(DIV_BY_ZERO) \
  : (UNLIKELY((x) == min && (y) == -1)) ? 0                 \
  : (ut)((x) % (y)))

#define I32_DIV_S(x, y) DIV_S(u32, INT32_MIN, (s32)x, (s32)y)
#define I64_DIV_S(x, y) DIV_S(u64, INT64_MIN, (s64)x, (s64)y)
#define I32_REM_S(x, y) REM_S(u32, INT32_MIN, (s32)x, (s32)y)
#define I64_REM_S(x, y) REM_S(u64, INT64_MIN, (s64)x, (s64)y)

#define DIVREM_U(op, x, y) \
  ((UNLIKELY((y) == 0)) ? TRAP(DIV_BY_ZERO) : ((x) op (y)))

#define DIV_U(x, y) DIVREM_U(/, x, y)
#define REM_U(x, y) DIVREM_U(%, x, y)

#define ROTL(x, y, mask) \
  (((x) << ((y) & (mask))) | ((x) >> (((mask) - (y) + 1) & (mask))))
#define ROTR(x, y, mask) \
  (((x) >> ((y) & (mask))) | ((x) << (((mask) - (y) + 1) & (mask))))

#define I32_ROTL(x, y) ROTL(x, y, 31)
#define I64_ROTL(x, y) ROTL(x, y, 63)
#define I32_ROTR(x, y) ROTR(x, y, 31)
#define I64_ROTR(x, y) ROTR(x, y, 63)

#define FMIN(x, y)                                          \
   ((UNLIKELY((x) != (x))) ? NAN                            \
  : (UNLIKELY((y) != (y))) ? NAN                            \
  : (UNLIKELY((x) == 0 && (y) == 0)) ? (signbit(x) ? x : y) \
  : (x < y) ? x : y)

#define FMAX(x, y)                                          \
   ((UNLIKELY((x) != (x))) ? NAN                            \
  : (UNLIKELY((y) != (y))) ? NAN                            \
  : (UNLIKELY((x) == 0 && (y) == 0)) ? (signbit(x) ? y : x) \
  : (x > y) ? x : y)

#define TRUNC_S(ut, st, ft, min, max, maxop, x)                             \
   ((UNLIKELY((x) != (x))) ? TRAP(INVALID_CONVERSION)                       \
  : (UNLIKELY((x) < (ft)(min) || (x) maxop (ft)(max))) ? TRAP(INT_OVERFLOW) \
  : (ut)(st)(x))

#define I32_TRUNC_S_F32(x) TRUNC_S(u32, s32, f32, INT32_MIN, INT32_MAX, >=, x)
#define I64_TRUNC_S_F32(x) TRUNC_S(u64, s64, f32, INT64_MIN, INT64_MAX, >=, x)
#define I32_TRUNC_S_F64(x) TRUNC_S(u32, s32, f64, INT32_MIN, INT32_MAX, >,  x)
#define I64_TRUNC_S_F64(x) TRUNC_S(u64, s64, f64, INT64_MIN, INT64_MAX, >=, x)

#define TRUNC_U(ut, ft, max, maxop, x)                                    \
   ((UNLIKELY((x) != (x))) ? TRAP(INVALID_CONVERSION)                     \
  : (UNLIKELY((x) <= (ft)-1 || (x) maxop (ft)(max))) ? TRAP(INT_OVERFLOW) \
  : (ut)(x))

#define I32_TRUNC_U_F32(x) TRUNC_U(u32, f32, UINT32_MAX, >=, x)
#define I64_TRUNC_U_F32(x) TRUNC_U(u64, f32, UINT64_MAX, >=, x)
#define I32_TRUNC_U_F64(x) TRUNC_U(u32, f64, UINT32_MAX, >,  x)
#define I64_TRUNC_U_F64(x) TRUNC_U(u64, f64, UINT64_MAX, >=, x)

#define DEFINE_REINTERPRET(name, t1, t2)  \
  static inline t2 name(t1 x) {           \
    t2 result;                            \
    memcpy(&result, &x, sizeof(result));  \
    return result;                        \
  }

DEFINE_REINTERPRET(f32_reinterpret_i32, u32, f32)
DEFINE_REINTERPRET(i32_reinterpret_f32, f32, u32)
DEFINE_REINTERPRET(f64_reinterpret_i64, u64, f64)
DEFINE_REINTERPRET(i64_reinterpret_f64, f64, u64)


static u32 func_types[7];

static void init_func_types(void) {
  func_types[0] = wasm_rt_register_func_type(1, 0, WASM_RT_I32);
  func_types[1] = wasm_rt_register_func_type(1, 1, WASM_RT_I32, WASM_RT_I32);
  func_types[2] = wasm_rt_register_func_type(0, 1, WASM_RT_I32);
  func_types[3] = wasm_rt_register_func_type(2, 0, WASM_RT_I32, WASM_RT_I32);
  func_types[4] = wasm_rt_register_func_type(4, 0, WASM_RT_I32, WASM_RT_I32, WASM_RT_I32, WASM_RT_I32);
  func_types[5] = wasm_rt_register_func_type(0, 0);
  func_types[6] = wasm_rt_register_func_type(0, 1, WASM_RT_F64);
}

static u32 f3(u32);
static u32 f4(void);
static void f5(u32);
static void f6(u32, u32);
static void f7(u32, u32);
static void _EncryptCBC(u32, u32, u32, u32);
static u32 f9(u32);
static void f10(u32, u32);
static void f11(u32, u32);
static u32 _check(u32);
static void runPostSets(void);
static void __post_instantiate(void);
static f64 f15(void);

static u32 g7;
static u32 g8;
static u32 g9;
static u32 g10;
static u32 g11;
static u32 g12;
static u32 g13;
static u32 g14;
static u32 g15;
static f64 g16;
static f64 g17;
static u32 g18;
static u32 g19;
static u32 g20;
static u32 g21;
static f64 g22;
static u32 g23;
static f32 g24;
static f32 g25;

static void init_globals(void) {
  g7 = (*Z_envZ_DYNAMICTOP_PTRZ_i);
  g8 = (*Z_envZ_tempDoublePtrZ_i);
  g9 = (*Z_envZ_ABORTZ_i);
  g10 = 0u;
  g11 = 0u;
  g12 = 0u;
  g13 = 0u;
  g14 = 0u;
  g15 = 0u;
  g16 = (*Z_globalZ_NaNZ_d);
  g17 = (*Z_globalZ_InfinityZ_d);
  g18 = 0u;
  g19 = 0u;
  g20 = 0u;
  g21 = 0u;
  g22 = 0;
  g23 = 0u;
  g24 = 0;
  g25 = 0;
}

static u32 f3(u32 p0) {
  u32 l0 = 0;
  FUNC_PROLOGUE;
  u32 i0, i1;
  i0 = g10;
  l0 = i0;
  i0 = g10;
  i1 = p0;
  i0 += i1;
  g10 = i0;
  i0 = g10;
  i1 = 15u;
  i0 += i1;
  i1 = 4294967280u;
  i0 &= i1;
  g10 = i0;
  i0 = g10;
  i1 = g11;
  i0 = (u32)((s32)i0 >= (s32)i1);
  if (i0) {
    i0 = p0;
    (*Z_envZ_abortStackOverflowZ_vi)(i0);
  }
  i0 = l0;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
  return i0;
}

static u32 f4(void) {
  FUNC_PROLOGUE;
  u32 i0;
  i0 = g10;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
  return i0;
}

static void f5(u32 p0) {
  FUNC_PROLOGUE;
  u32 i0;
  i0 = p0;
  g10 = i0;
  FUNC_EPILOGUE;
}

static void f6(u32 p0, u32 p1) {
  FUNC_PROLOGUE;
  u32 i0;
  i0 = p0;
  g10 = i0;
  i0 = p1;
  g11 = i0;
  FUNC_EPILOGUE;
}

static void f7(u32 p0, u32 p1) {
  FUNC_PROLOGUE;
  u32 i0, i1;
  i0 = g12;
  i1 = 0u;
  i0 = i0 == i1;
  if (i0) {
    i0 = p0;
    g12 = i0;
    i0 = p1;
    g13 = i0;
  }
  FUNC_EPILOGUE;
}

static void _EncryptCBC(u32 p0, u32 p1, u32 p2, u32 p3) {
  u32 l0 = 0, l1 = 0, l2 = 0, l3 = 0, l4 = 0, l5 = 0, l6 = 0, l7 = 0, 
      l8 = 0, l9 = 0, l10 = 0, l11 = 0, l12 = 0, l13 = 0, l14 = 0, l15 = 0, 
      l16 = 0, l17 = 0, l18 = 0, l19 = 0, l20 = 0, l21 = 0, l22 = 0, l23 = 0, 
      l24 = 0, l25 = 0, l26 = 0, l27 = 0, l28 = 0, l29 = 0, l30 = 0, l31 = 0, 
      l32 = 0, l33 = 0, l34 = 0, l35 = 0, l36 = 0, l37 = 0, l38 = 0, l39 = 0, 
      l40 = 0, l41 = 0;
  FUNC_PROLOGUE;
  u32 i0, i1;
  i0 = g10;
  l41 = i0;
  i0 = g10;
  i1 = 48u;
  i0 += i1;
  g10 = i0;
  i0 = g10;
  i1 = g11;
  i0 = (u32)((s32)i0 >= (s32)i1);
  if (i0) {
    i0 = 48u;
    (*Z_envZ_abortStackOverflowZ_vi)(i0);
  }
  i0 = l41;
  i1 = 16u;
  i0 += i1;
  l38 = i0;
  i0 = l41;
  l39 = i0;
  i0 = p0;
  l30 = i0;
  i0 = p1;
  l35 = i0;
  i0 = p2;
  l36 = i0;
  i0 = p3;
  l37 = i0;
  i0 = l37;
  l0 = i0;
  i0 = l0;
  i0 = f9(i0);
  l1 = i0;
  i0 = l39;
  i1 = l1;
  i32_store(Z_envZ_memory, (u64)(i0), i1);
  i0 = l37;
  l2 = i0;
  i0 = l2;
  i1 = 4u;
  i0 += i1;
  l3 = i0;
  i0 = l3;
  i0 = f9(i0);
  l4 = i0;
  i0 = l39;
  i1 = 4u;
  i0 += i1;
  l5 = i0;
  i0 = l5;
  i1 = l4;
  i32_store(Z_envZ_memory, (u64)(i0), i1);
  i0 = l37;
  l6 = i0;
  i0 = l6;
  i1 = 8u;
  i0 += i1;
  l7 = i0;
  i0 = l7;
  i0 = f9(i0);
  l8 = i0;
  i0 = l39;
  i1 = 8u;
  i0 += i1;
  l9 = i0;
  i0 = l9;
  i1 = l8;
  i32_store(Z_envZ_memory, (u64)(i0), i1);
  i0 = l37;
  l10 = i0;
  i0 = l10;
  i1 = 12u;
  i0 += i1;
  l11 = i0;
  i0 = l11;
  i0 = f9(i0);
  l12 = i0;
  i0 = l39;
  i1 = 12u;
  i0 += i1;
  l13 = i0;
  i0 = l13;
  i1 = l12;
  i32_store(Z_envZ_memory, (u64)(i0), i1);
  L1: 
    i0 = l36;
    l14 = i0;
    i0 = l14;
    i1 = 8u;
    i0 = (u32)((s32)i0 >= (s32)i1);
    l15 = i0;
    i0 = l15;
    i0 = !(i0);
    if (i0) {
      goto B2;
    }
    i0 = l35;
    l16 = i0;
    i0 = l16;
    i0 = f9(i0);
    l17 = i0;
    i0 = l38;
    i1 = l17;
    i32_store(Z_envZ_memory, (u64)(i0), i1);
    i0 = l35;
    l18 = i0;
    i0 = l18;
    i1 = 4u;
    i0 += i1;
    l19 = i0;
    i0 = l19;
    i0 = f9(i0);
    l20 = i0;
    i0 = l38;
    i1 = 4u;
    i0 += i1;
    l21 = i0;
    i0 = l21;
    i1 = l20;
    i32_store(Z_envZ_memory, (u64)(i0), i1);
    i0 = l38;
    i1 = l39;
    f10(i0, i1);
    i0 = l30;
    l22 = i0;
    i0 = l38;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l23 = i0;
    i0 = l22;
    i1 = l23;
    f11(i0, i1);
    i0 = l30;
    l24 = i0;
    i0 = l24;
    i1 = 4u;
    i0 += i1;
    l25 = i0;
    i0 = l38;
    i1 = 4u;
    i0 += i1;
    l26 = i0;
    i0 = l26;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l27 = i0;
    i0 = l25;
    i1 = l27;
    f11(i0, i1);
    i0 = l35;
    l28 = i0;
    i0 = l28;
    i1 = 8u;
    i0 += i1;
    l29 = i0;
    i0 = l29;
    l35 = i0;
    i0 = l30;
    l31 = i0;
    i0 = l31;
    i1 = 8u;
    i0 += i1;
    l32 = i0;
    i0 = l32;
    l30 = i0;
    i0 = l36;
    l33 = i0;
    i0 = l33;
    i1 = 8u;
    i0 -= i1;
    l34 = i0;
    i0 = l34;
    l36 = i0;
    goto L1;
    B2:;
  i0 = l41;
  g10 = i0;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
}

static u32 f9(u32 p0) {
  u32 l0 = 0, l1 = 0, l2 = 0, l3 = 0, l4 = 0, l5 = 0, l6 = 0, l7 = 0, 
      l8 = 0, l9 = 0, l10 = 0, l11 = 0, l12 = 0, l13 = 0, l14 = 0, l15 = 0, 
      l16 = 0, l17 = 0, l18 = 0, l19 = 0, l20 = 0, l21 = 0, l22 = 0, l23 = 0;
  FUNC_PROLOGUE;
  u32 i0, i1;
  i0 = g10;
  l23 = i0;
  i0 = g10;
  i1 = 16u;
  i0 += i1;
  g10 = i0;
  i0 = g10;
  i1 = g11;
  i0 = (u32)((s32)i0 >= (s32)i1);
  if (i0) {
    i0 = 16u;
    (*Z_envZ_abortStackOverflowZ_vi)(i0);
  }
  i0 = p0;
  l0 = i0;
  i0 = l0;
  l11 = i0;
  i0 = l11;
  i0 = i32_load8_s(Z_envZ_memory, (u64)(i0));
  l15 = i0;
  i0 = l15;
  i1 = 255u;
  i0 &= i1;
  l16 = i0;
  i0 = l0;
  l17 = i0;
  i0 = l17;
  i1 = 1u;
  i0 += i1;
  l18 = i0;
  i0 = l18;
  i0 = i32_load8_s(Z_envZ_memory, (u64)(i0));
  l19 = i0;
  i0 = l19;
  i1 = 255u;
  i0 &= i1;
  l20 = i0;
  i0 = l20;
  i1 = 8u;
  i0 <<= (i1 & 31);
  l21 = i0;
  i0 = l16;
  i1 = l21;
  i0 |= i1;
  l1 = i0;
  i0 = l0;
  l2 = i0;
  i0 = l2;
  i1 = 2u;
  i0 += i1;
  l3 = i0;
  i0 = l3;
  i0 = i32_load8_s(Z_envZ_memory, (u64)(i0));
  l4 = i0;
  i0 = l4;
  i1 = 255u;
  i0 &= i1;
  l5 = i0;
  i0 = l5;
  i1 = 16u;
  i0 <<= (i1 & 31);
  l6 = i0;
  i0 = l1;
  i1 = l6;
  i0 |= i1;
  l7 = i0;
  i0 = l0;
  l8 = i0;
  i0 = l8;
  i1 = 3u;
  i0 += i1;
  l9 = i0;
  i0 = l9;
  i0 = i32_load8_s(Z_envZ_memory, (u64)(i0));
  l10 = i0;
  i0 = l10;
  i1 = 255u;
  i0 &= i1;
  l12 = i0;
  i0 = l12;
  i1 = 24u;
  i0 <<= (i1 & 31);
  l13 = i0;
  i0 = l7;
  i1 = l13;
  i0 |= i1;
  l14 = i0;
  i0 = l23;
  g10 = i0;
  i0 = l14;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
  return i0;
}

static void f10(u32 p0, u32 p1) {
  u32 l0 = 0, l1 = 0, l2 = 0, l3 = 0, l4 = 0, l5 = 0, l6 = 0, l7 = 0, 
      l8 = 0, l9 = 0, l10 = 0, l11 = 0, l12 = 0, l13 = 0, l14 = 0, l15 = 0, 
      l16 = 0, l17 = 0, l18 = 0, l19 = 0, l20 = 0, l21 = 0, l22 = 0, l23 = 0, 
      l24 = 0, l25 = 0, l26 = 0, l27 = 0, l28 = 0, l29 = 0, l30 = 0, l31 = 0, 
      l32 = 0, l33 = 0, l34 = 0, l35 = 0, l36 = 0, l37 = 0, l38 = 0, l39 = 0, 
      l40 = 0, l41 = 0, l42 = 0, l43 = 0, l44 = 0, l45 = 0, l46 = 0, l47 = 0, 
      l48 = 0, l49 = 0, l50 = 0, l51 = 0, l52 = 0, l53 = 0, l54 = 0, l55 = 0, 
      l56 = 0, l57 = 0, l58 = 0, l59 = 0, l60 = 0, l61 = 0, l62 = 0;
  FUNC_PROLOGUE;
  u32 i0, i1;
  i0 = g10;
  l62 = i0;
  i0 = g10;
  i1 = 32u;
  i0 += i1;
  g10 = i0;
  i0 = g10;
  i1 = g11;
  i0 = (u32)((s32)i0 >= (s32)i1);
  if (i0) {
    i0 = 32u;
    (*Z_envZ_abortStackOverflowZ_vi)(i0);
  }
  i0 = p0;
  l10 = i0;
  i0 = p1;
  l21 = i0;
  i0 = 2654435769u;
  l32 = i0;
  i0 = 0u;
  l43 = i0;
  i0 = 0u;
  l54 = i0;
  L1: 
    i0 = l54;
    l58 = i0;
    i0 = l58;
    i1 = 32u;
    i0 = i0 < i1;
    l59 = i0;
    i0 = l59;
    i0 = !(i0);
    if (i0) {
      goto B2;
    }
    i0 = l32;
    l60 = i0;
    i0 = l43;
    l0 = i0;
    i0 = l0;
    i1 = l60;
    i0 += i1;
    l1 = i0;
    i0 = l1;
    l43 = i0;
    i0 = l10;
    l2 = i0;
    i0 = l2;
    i1 = 4u;
    i0 += i1;
    l3 = i0;
    i0 = l3;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l4 = i0;
    i0 = l4;
    i1 = 3u;
    i0 <<= (i1 & 31);
    l5 = i0;
    i0 = l21;
    l6 = i0;
    i0 = l6;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l7 = i0;
    i0 = l5;
    i1 = l7;
    i0 ^= i1;
    l8 = i0;
    i0 = l10;
    l9 = i0;
    i0 = l9;
    i1 = 4u;
    i0 += i1;
    l11 = i0;
    i0 = l11;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l12 = i0;
    i0 = l43;
    l13 = i0;
    i0 = l12;
    i1 = l13;
    i0 += i1;
    l14 = i0;
    i0 = l8;
    i1 = l14;
    i0 ^= i1;
    l15 = i0;
    i0 = l10;
    l16 = i0;
    i0 = l16;
    i1 = 4u;
    i0 += i1;
    l17 = i0;
    i0 = l17;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l18 = i0;
    i0 = l18;
    i1 = 5u;
    i0 >>= (i1 & 31);
    l19 = i0;
    i0 = l21;
    l20 = i0;
    i0 = l20;
    i1 = 4u;
    i0 += i1;
    l22 = i0;
    i0 = l22;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l23 = i0;
    i0 = l19;
    i1 = l23;
    i0 += i1;
    l24 = i0;
    i0 = l15;
    i1 = l24;
    i0 ^= i1;
    l25 = i0;
    i0 = l10;
    l26 = i0;
    i0 = l26;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l27 = i0;
    i0 = l27;
    i1 = l25;
    i0 += i1;
    l28 = i0;
    i0 = l26;
    i1 = l28;
    i32_store(Z_envZ_memory, (u64)(i0), i1);
    i0 = l10;
    l29 = i0;
    i0 = l29;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l30 = i0;
    i0 = l30;
    i1 = 3u;
    i0 <<= (i1 & 31);
    l31 = i0;
    i0 = l21;
    l33 = i0;
    i0 = l33;
    i1 = 8u;
    i0 += i1;
    l34 = i0;
    i0 = l34;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l35 = i0;
    i0 = l31;
    i1 = l35;
    i0 ^= i1;
    l36 = i0;
    i0 = l10;
    l37 = i0;
    i0 = l37;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l38 = i0;
    i0 = l43;
    l39 = i0;
    i0 = l38;
    i1 = l39;
    i0 += i1;
    l40 = i0;
    i0 = l36;
    i1 = l40;
    i0 ^= i1;
    l41 = i0;
    i0 = l10;
    l42 = i0;
    i0 = l42;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l44 = i0;
    i0 = l44;
    i1 = 5u;
    i0 >>= (i1 & 31);
    l45 = i0;
    i0 = l21;
    l46 = i0;
    i0 = l46;
    i1 = 12u;
    i0 += i1;
    l47 = i0;
    i0 = l47;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l48 = i0;
    i0 = l45;
    i1 = l48;
    i0 += i1;
    l49 = i0;
    i0 = l41;
    i1 = l49;
    i0 ^= i1;
    l50 = i0;
    i0 = l10;
    l51 = i0;
    i0 = l51;
    i1 = 4u;
    i0 += i1;
    l52 = i0;
    i0 = l52;
    i0 = i32_load(Z_envZ_memory, (u64)(i0));
    l53 = i0;
    i0 = l53;
    i1 = l50;
    i0 += i1;
    l55 = i0;
    i0 = l52;
    i1 = l55;
    i32_store(Z_envZ_memory, (u64)(i0), i1);
    i0 = l54;
    l56 = i0;
    i0 = l56;
    i1 = 1u;
    i0 += i1;
    l57 = i0;
    i0 = l57;
    l54 = i0;
    goto L1;
    B2:;
  i0 = l62;
  g10 = i0;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
}

static void f11(u32 p0, u32 p1) {
  u32 l0 = 0, l1 = 0, l2 = 0, l3 = 0, l4 = 0, l5 = 0, l6 = 0, l7 = 0, 
      l8 = 0, l9 = 0, l10 = 0, l11 = 0, l12 = 0, l13 = 0, l14 = 0, l15 = 0, 
      l16 = 0, l17 = 0, l18 = 0, l19 = 0, l20 = 0, l21 = 0;
  FUNC_PROLOGUE;
  u32 i0, i1;
  i0 = g10;
  l21 = i0;
  i0 = g10;
  i1 = 16u;
  i0 += i1;
  g10 = i0;
  i0 = g10;
  i1 = g11;
  i0 = (u32)((s32)i0 >= (s32)i1);
  if (i0) {
    i0 = 16u;
    (*Z_envZ_abortStackOverflowZ_vi)(i0);
  }
  i0 = p0;
  l10 = i0;
  i0 = p1;
  l13 = i0;
  i0 = l13;
  l14 = i0;
  i0 = l14;
  i1 = 255u;
  i0 &= i1;
  l15 = i0;
  i0 = l10;
  l16 = i0;
  i0 = l16;
  i1 = l15;
  i32_store8(Z_envZ_memory, (u64)(i0), i1);
  i0 = l13;
  l17 = i0;
  i0 = l17;
  i1 = 8u;
  i0 >>= (i1 & 31);
  l18 = i0;
  i0 = l18;
  i1 = 255u;
  i0 &= i1;
  l19 = i0;
  i0 = l10;
  l0 = i0;
  i0 = l0;
  i1 = 1u;
  i0 += i1;
  l1 = i0;
  i0 = l1;
  i1 = l19;
  i32_store8(Z_envZ_memory, (u64)(i0), i1);
  i0 = l13;
  l2 = i0;
  i0 = l2;
  i1 = 16u;
  i0 >>= (i1 & 31);
  l3 = i0;
  i0 = l3;
  i1 = 255u;
  i0 &= i1;
  l4 = i0;
  i0 = l10;
  l5 = i0;
  i0 = l5;
  i1 = 2u;
  i0 += i1;
  l6 = i0;
  i0 = l6;
  i1 = l4;
  i32_store8(Z_envZ_memory, (u64)(i0), i1);
  i0 = l13;
  l7 = i0;
  i0 = l7;
  i1 = 24u;
  i0 >>= (i1 & 31);
  l8 = i0;
  i0 = l8;
  i1 = 255u;
  i0 &= i1;
  l9 = i0;
  i0 = l10;
  l11 = i0;
  i0 = l11;
  i1 = 3u;
  i0 += i1;
  l12 = i0;
  i0 = l12;
  i1 = l9;
  i32_store8(Z_envZ_memory, (u64)(i0), i1);
  i0 = l21;
  g10 = i0;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
}

static u32 _check(u32 p0) {
  u32 l0 = 0, l1 = 0, l2 = 0, l3 = 0, l4 = 0, l5 = 0, l6 = 0, l7 = 0, 
      l8 = 0, l9 = 0, l10 = 0, l11 = 0, l12 = 0, l13 = 0, l14 = 0, l15 = 0, 
      l16 = 0, l17 = 0, l18 = 0, l19 = 0, l20 = 0, l21 = 0, l22 = 0, l23 = 0, 
      l24 = 0, l25 = 0, l26 = 0, l27 = 0, l28 = 0, l29 = 0, l30 = 0, l31 = 0, 
      l32 = 0, l33 = 0, l34 = 0, l35 = 0, l36 = 0, l37 = 0, l38 = 0;
  FUNC_PROLOGUE;
  u32 i0, i1, i2, i3;
  i0 = g10;
  l36 = i0;
  i0 = g10;
  i1 = 160u;
  i0 += i1;
  g10 = i0;
  i0 = g10;
  i1 = g11;
  i0 = (u32)((s32)i0 >= (s32)i1);
  if (i0) {
    i0 = 160u;
    (*Z_envZ_abortStackOverflowZ_vi)(i0);
  }
  i0 = l36;
  i1 = 144u;
  i0 += i1;
  l22 = i0;
  i0 = l36;
  i1 = 120u;
  i0 += i1;
  l28 = i0;
  i0 = l36;
  i1 = 8u;
  i0 += i1;
  l30 = i0;
  i0 = p0;
  l11 = i0;
  i0 = l11;
  l32 = i0;
  i0 = l32;
  i0 = (*Z_envZ__strlenZ_ii)(i0);
  l33 = i0;
  i0 = l33;
  i1 = 24u;
  i0 = i0 != i1;
  l1 = i0;
  i0 = l1;
  if (i0) {
    i0 = 0u;
    l0 = i0;
    i0 = l0;
    l27 = i0;
    i0 = l36;
    g10 = i0;
    i0 = l27;
    goto Bfunc;
  }
  i0 = l22;
  l34 = i0;
  i0 = (*Z_envZ_memoryBaseZ_i);
  i1 = 96u;
  i0 += i1;
  l37 = i0;
  i0 = l34;
  i1 = 16u;
  i0 += i1;
  l38 = i0;
  L2: 
    i0 = l34;
    i1 = l37;
    i1 = i32_load8_s(Z_envZ_memory, (u64)(i1));
    i32_store8(Z_envZ_memory, (u64)(i0), i1);
    i0 = l34;
    i1 = 1u;
    i0 += i1;
    l34 = i0;
    i0 = l37;
    i1 = 1u;
    i0 += i1;
    l37 = i0;
    i0 = l34;
    i1 = l38;
    i0 = (u32)((s32)i0 < (s32)i1);
    if (i0) {goto L2;}
  i0 = l11;
  l2 = i0;
  i0 = l28;
  i1 = l2;
  i2 = 4u;
  i3 = l22;
  _EncryptCBC(i0, i1, i2, i3);
  i0 = 0u;
  l29 = i0;
  i0 = l30;
  l34 = i0;
  i0 = (*Z_envZ_memoryBaseZ_i);
  i1 = 0u;
  i0 += i1;
  l37 = i0;
  i0 = l34;
  i1 = 96u;
  i0 += i1;
  l38 = i0;
  L3: 
    i0 = l34;
    i1 = l37;
    i1 = i32_load(Z_envZ_memory, (u64)(i1));
    i32_store(Z_envZ_memory, (u64)(i0), i1);
    i0 = l34;
    i1 = 4u;
    i0 += i1;
    l34 = i0;
    i0 = l37;
    i1 = 4u;
    i0 += i1;
    l37 = i0;
    i0 = l34;
    i1 = l38;
    i0 = (u32)((s32)i0 < (s32)i1);
    if (i0) {goto L3;}
  i0 = 0u;
  l29 = i0;
  L4: 
    i0 = l29;
    l3 = i0;
    i0 = l3;
    i1 = 3u;
    i0 = (u32)((s32)i0 < (s32)i1);
    l4 = i0;
    i0 = l4;
    i0 = !(i0);
    if (i0) {
      i0 = 11u;
      l35 = i0;
      goto B5;
    }
    i0 = 0u;
    l31 = i0;
    L7: 
      i0 = l31;
      l5 = i0;
      i0 = l5;
      i1 = 8u;
      i0 = (u32)((s32)i0 < (s32)i1);
      l6 = i0;
      i0 = l29;
      l7 = i0;
      i0 = l6;
      i0 = !(i0);
      if (i0) {
        goto B8;
      }
      i0 = l7;
      i1 = 3u;
      i0 <<= (i1 & 31);
      l8 = i0;
      i0 = l31;
      l9 = i0;
      i0 = l8;
      i1 = l9;
      i0 += i1;
      l10 = i0;
      i0 = l28;
      i1 = l10;
      i0 += i1;
      l12 = i0;
      i0 = l12;
      i0 = i32_load8_s(Z_envZ_memory, (u64)(i0));
      l13 = i0;
      i0 = l13;
      i1 = 255u;
      i0 &= i1;
      l14 = i0;
      i0 = l29;
      l15 = i0;
      i0 = l15;
      i1 = 3u;
      i0 <<= (i1 & 31);
      l16 = i0;
      i0 = l16;
      i1 = 7u;
      i0 += i1;
      l17 = i0;
      i0 = l31;
      l18 = i0;
      i0 = l17;
      i1 = l18;
      i0 -= i1;
      l19 = i0;
      i0 = l30;
      i1 = l19;
      i2 = 2u;
      i1 <<= (i2 & 31);
      i0 += i1;
      l20 = i0;
      i0 = l20;
      i0 = i32_load(Z_envZ_memory, (u64)(i0));
      l21 = i0;
      i0 = l14;
      i1 = l21;
      i0 = i0 != i1;
      l23 = i0;
      i0 = l23;
      if (i0) {
        i0 = 8u;
        l35 = i0;
        goto B5;
      }
      i0 = l31;
      l24 = i0;
      i0 = l24;
      i1 = 1u;
      i0 += i1;
      l25 = i0;
      i0 = l25;
      l31 = i0;
      goto L7;
      B8:;
    i0 = l7;
    i1 = 1u;
    i0 += i1;
    l26 = i0;
    i0 = l26;
    l29 = i0;
    goto L4;
    B5:;
  i0 = l35;
  i1 = 8u;
  i0 = i0 == i1;
  if (i0) {
    i0 = 0u;
    l0 = i0;
    i0 = l0;
    l27 = i0;
    i0 = l36;
    g10 = i0;
    i0 = l27;
    goto Bfunc;
  } else {
    i0 = l35;
    i1 = 11u;
    i0 = i0 == i1;
    if (i0) {
      i0 = 1u;
      l0 = i0;
      i0 = l0;
      l27 = i0;
      i0 = l36;
      g10 = i0;
      i0 = l27;
      goto Bfunc;
    }
  }
  i0 = 0u;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
  return i0;
}

static void runPostSets(void) {
  u32 l0 = 0;
  FUNC_PROLOGUE;
  FUNC_EPILOGUE;
}

static void __post_instantiate(void) {
  FUNC_PROLOGUE;
  u32 i0, i1;
  i0 = (*Z_envZ_memoryBaseZ_i);
  i1 = 112u;
  i0 += i1;
  g10 = i0;
  i0 = g10;
  i1 = 5242880u;
  i0 += i1;
  g11 = i0;
  runPostSets();
  FUNC_EPILOGUE;
}

static f64 f15(void) {
  FUNC_PROLOGUE;
  u32 i0;
  f64 d0;
  i0 = 0u;
  (*Z_envZ_nullFunc_XZ_vi)(i0);
  d0 = 0;
  goto Bfunc;
  Bfunc:;
  FUNC_EPILOGUE;
  return d0;
}

static const u8 data_segment_data_0[] = {
  0x99, 0x00, 0x00, 0x00, 0x77, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 
  0xbd, 0x00, 0x00, 0x00, 0x2f, 0x00, 0x00, 0x00, 0x6c, 0x00, 0x00, 0x00, 
  0x87, 0x00, 0x00, 0x00, 0x35, 0x00, 0x00, 0x00, 0x55, 0x00, 0x00, 0x00, 
  0x22, 0x00, 0x00, 0x00, 0x79, 0x00, 0x00, 0x00, 0x1d, 0x00, 0x00, 0x00, 
  0xf6, 0x00, 0x00, 0x00, 0x48, 0x00, 0x00, 0x00, 0x2c, 0x00, 0x00, 0x00, 
  0x8c, 0x00, 0x00, 0x00, 0xb9, 0x00, 0x00, 0x00, 0xd6, 0x00, 0x00, 0x00, 
  0x13, 0x00, 0x00, 0x00, 0x93, 0x00, 0x00, 0x00, 0xcb, 0x00, 0x00, 0x00, 
  0xd8, 0x00, 0x00, 0x00, 0x31, 0x00, 0x00, 0x00, 0xe3, 0x00, 0x00, 0x00, 
  0x77, 0x65, 0x62, 0x61, 0x73, 0x6d, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x73, 
  0x74, 0x69, 0x6e, 0x67, 
};

static void init_memory(void) {
  memcpy(&((*Z_envZ_memory).data[(*Z_envZ_memoryBaseZ_i)]), data_segment_data_0, 112);
}

static void init_table(void) {
  uint32_t offset;
  offset = (*Z_envZ_tableBaseZ_i);
  (*Z_envZ_table).data[offset + 0] = (wasm_rt_elem_t){func_types[6], (wasm_rt_anyfunc_t)(&f15)};
  (*Z_envZ_table).data[offset + 1] = (wasm_rt_elem_t){func_types[4], (wasm_rt_anyfunc_t)(&_EncryptCBC)};
  (*Z_envZ_table).data[offset + 2] = (wasm_rt_elem_t){func_types[1], (wasm_rt_anyfunc_t)(&_check)};
  (*Z_envZ_table).data[offset + 3] = (wasm_rt_elem_t){func_types[6], (wasm_rt_anyfunc_t)(&f15)};
}

/* export: '_EncryptCBC' */
void (*WASM_RT_ADD_PREFIX(Z__EncryptCBCZ_viiii))(u32, u32, u32, u32);
/* export: '__post_instantiate' */
void (*WASM_RT_ADD_PREFIX(Z___post_instantiateZ_vv))(void);
/* export: '_check' */
u32 (*WASM_RT_ADD_PREFIX(Z__checkZ_ii))(u32);
/* export: 'runPostSets' */
void (*WASM_RT_ADD_PREFIX(Z_runPostSetsZ_vv))(void);

static void init_exports(void) {
  /* export: '_EncryptCBC' */
  WASM_RT_ADD_PREFIX(Z__EncryptCBCZ_viiii) = (&_EncryptCBC);
  /* export: '__post_instantiate' */
  WASM_RT_ADD_PREFIX(Z___post_instantiateZ_vv) = (&__post_instantiate);
  /* export: '_check' */
  WASM_RT_ADD_PREFIX(Z__checkZ_ii) = (&_check);
  /* export: 'runPostSets' */
  WASM_RT_ADD_PREFIX(Z_runPostSetsZ_vv) = (&runPostSets);
}

void WASM_RT_ADD_PREFIX(init)(void) {
  init_func_types();
  init_globals();
  init_memory();
  init_table();
  init_exports();
}
