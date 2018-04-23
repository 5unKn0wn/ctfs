#ifndef _HOME_5UNKN0WN_CTFS_2018__CTF_CHECK_H_GENERATED_
#define _HOME_5UNKN0WN_CTFS_2018__CTF_CHECK_H_GENERATED_
#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

#include "wasm-rt.h"

#ifndef WASM_RT_MODULE_PREFIX
#define WASM_RT_MODULE_PREFIX
#endif

#define WASM_RT_PASTE_(x, y) x ## y
#define WASM_RT_PASTE(x, y) WASM_RT_PASTE_(x, y)
#define WASM_RT_ADD_PREFIX(x) WASM_RT_PASTE(WASM_RT_MODULE_PREFIX, x)

#define WASM_RT_DEFINE_EXTERNAL(decl, target) decl = &target;

/* TODO(binji): only use stdint.h types in header */
typedef uint8_t u8;
typedef int8_t s8;
typedef uint16_t u16;
typedef int16_t s16;
typedef uint32_t u32;
typedef int32_t s32;
typedef uint64_t u64;
typedef int64_t s64;
typedef float f32;
typedef double f64;

extern void WASM_RT_ADD_PREFIX(init)(void);

/* import: 'env' 'memory' */
extern wasm_rt_memory_t (*Z_envZ_memory);
/* import: 'env' 'table' */
extern wasm_rt_table_t (*Z_envZ_table);
/* import: 'env' 'memoryBase' */
extern u32 (*Z_envZ_memoryBaseZ_i);
/* import: 'env' 'tableBase' */
extern u32 (*Z_envZ_tableBaseZ_i);
/* import: 'env' 'DYNAMICTOP_PTR' */
extern u32 (*Z_envZ_DYNAMICTOP_PTRZ_i);
/* import: 'env' 'tempDoublePtr' */
extern u32 (*Z_envZ_tempDoublePtrZ_i);
/* import: 'env' 'ABORT' */
extern u32 (*Z_envZ_ABORTZ_i);
/* import: 'global' 'NaN' */
extern f64 (*Z_globalZ_NaNZ_d);
/* import: 'global' 'Infinity' */
extern f64 (*Z_globalZ_InfinityZ_d);
/* import: 'env' 'abortStackOverflow' */
extern void (*Z_envZ_abortStackOverflowZ_vi)(u32);
/* import: 'env' 'nullFunc_X' */
extern void (*Z_envZ_nullFunc_XZ_vi)(u32);
/* import: 'env' '_strlen' */
extern u32 (*Z_envZ__strlenZ_ii)(u32);

/* export: '_EncryptCBC' */
extern void (*WASM_RT_ADD_PREFIX(Z__EncryptCBCZ_viiii))(u32, u32, u32, u32);
/* export: '__post_instantiate' */
extern void (*WASM_RT_ADD_PREFIX(Z___post_instantiateZ_vv))(void);
/* export: '_check' */
extern u32 (*WASM_RT_ADD_PREFIX(Z__checkZ_ii))(u32);
/* export: 'runPostSets' */
extern void (*WASM_RT_ADD_PREFIX(Z_runPostSetsZ_vv))(void);
#ifdef __cplusplus
}
#endif

#endif  /* _HOME_5UNKN0WN_CTFS_2018__CTF_CHECK_H_GENERATED_ */
