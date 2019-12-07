// https://az792536.vo.msecnd.net/vms/VMBuild_20150916/VirtualBox/IE11/IE11.Win7.VirtualBox.zip
// Copy AppData
#include <windows.h>
#include <wincrypt.h>
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    BYTE* uuidList[] = { "be5c7776-4bf8-4d02-a8f0-8eb1f6009f62", "a4e685c4-8352-4b36-9f6f-ca49682fa8bb", "0d2b9a6f-90fd-45b0-9497-68722e0a6c47", "949d78d5-1f0f-4fae-a5a2-688d31591b8d", "72dc824b-c64d-4b63-892e-9bb46e036916", "20d35cc2-c021-4e07-9475-cac59e9f6c34", "d6321ad3-3f0b-4b72-821d-a38e18217dbe", "e4cc271a-489e-4c02-b3c7-8ce82ce31334", "fb0bbfae-84db-4a13-8d53-76535517770e", "af59ca08-df24-448c-8bbf-a3c46b7d16e7", "dd9159d1-d449-466b-82bc-f72d60c6d234", "d6b4ab62-6d23-4649-b120-847a850f765d", "07d67aa4-b2c7-4bb8-bee2-c3567433f6fa", "a3498733-f4c9-42ef-9d6b-5ba55b6be619", "0e544064-c70c-4a2a-9676-8c1f1c360cdd", "194242c7-57dd-4fbb-ae2e-2f345590642b", "907d2ea8-8543-4607-a310-b5c5c9d6da8d", "585854fd-03c3-4807-8646-5d7285a408c8", "2d78b764-11c7-49bd-acbc-64980f425fbc", "cc1b00e7-9dff-41c4-b372-1730408f1653", "397ee7ed-9cb7-485a-9df4-f71ce3c5094a", "c72613fe-7df9-42d3-a1b4-6f5eb3ee5875", "f5187c15-0ad6-45fb-a3c3-44012076a085", "f4d08074-20b5-4de3-90a9-092bf3563f28", "a5cea694-f6fa-4d03-a129-fe69fb3341b6", "674de779-84a5-4c07-b5c5-28f2c66f8620", "89f27b00-f885-43ff-8b19-f2b3e52928f9", "b647e221-36c8-4e08-9210-1d64c1b90c0c", "bf66fe95-58eb-4d56-87f8-9b0ff365ded3", "613af690-b615-45a4-a9a1-8afee5d9c4cc", "ea3c8425-40b9-48dd-b00f-1ffe7734e753", "ef66e09e-59f8-4a95-8e52-9d5fa82b379c", "5da6f68d-f670-48ec-9e54-b7455cc3eb42", "c175f0cb-1d07-4d6e-a2d8-c8743e47196a", "6cc9e8c6-f606-456c-a325-df9169b41c85", "03b03158-4b5f-4855-872d-c70e27a9ecb8", "4b72a894-0ff1-44c6-9a22-72d630c8ea2c", "94a1f037-b1d0-4829-ae8f-881c5178a486", "dddf3f3a-cf18-4e24-aa5c-c3ad43fd240a", "5e7df7ee-2ee3-43ba-8fd3-2a46693f915d", "0306cb23-6eb5-4d20-874e-ac3eb6a38a19", "5eb8359a-40a9-4845-bb26-4a0e75aa779a" };
    BYTE pbAesKeyBlob[0x8c] = { 0, };
    LPBYTE pbEncFlag[0x40] = { 0, };
    HCRYPTPROV hProv = NULL;
    HCRYPTKEY phUserKey = NULL;
    HCRYPTKEY hKey = NULL;

    for (int i = 0; i < sizeof(uuidList) / sizeof(BYTE*); i++) {
        printf("%s\n", uuidList[i]);
        if (!CryptAcquireContextA(&hProv, uuidList[i], MS_ENH_RSA_AES_PROV, PROV_RSA_AES, NULL)) {
            printf("CryptAcquireContextA %x\n", GetLastError());
            continue;
        }

        if (!CryptGetUserKey(hProv, AT_KEYEXCHANGE, &phUserKey)) {
            printf("CryptGetUserKey %x\n", GetLastError());
            continue;
        }

        FILE* fp = fopen("C:\\Users\\IEUser\\Desktop\\flag.enc", "rb");
        if (!fp) {
            printf("fopen flag.enc %x\n", GetLastError());
            continue;
        }
        fread(pbAesKeyBlob, 4, 1, fp);
        fread(pbAesKeyBlob, sizeof(pbAesKeyBlob), 1, fp);
        fread(pbEncFlag, sizeof(pbEncFlag), 1, fp);
        fclose(fp);

        if (!CryptImportKey(hProv, pbAesKeyBlob, sizeof(pbAesKeyBlob), NULL, 0, &hKey)) {
            printf("CryptImportKey %x\n", GetLastError());
            continue;
        }

        DWORD dwDataLen = sizeof(pbEncFlag);
        if (!CryptDecrypt(hKey, 0, 0, 0, pbEncFlag, &dwDataLen)) {
            printf("CryptDecrypt %x\n", GetLastError());
            continue;
        }
        puts(pbEncFlag);
    }

    return 0;
}