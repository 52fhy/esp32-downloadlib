# esp32-downloadlib

下载esp32-downloadlib.rar，解压后使用python运行。

外链:https://fuml.lanzouw.com/b0fpux0uj 密码:7sso

github: https://github.com/52fhy/esp32-downloadlib

```
D:\Download\esp32-downloadlib>python esp32-download.py
请选择 ESP32 版本：
  1. 3.3.1-cn
  2. 3.3.0-cn
  3. 3.2.1-cn
  4. 3.2.0-cn
  5. 3.1.3-cn
  6. 3.1.2-cn
  7. 3.1.1-cn
  8. 3.1.0-cn
  ...
输入序号：7

请选择系统版本：
  1. windows-32
  2. windows-64
  3. linux-64
  ...
输入序号：2

找到以下可下载项：
  esp32-platform : https://dl.espressif.cn/github_assets/espressif/arduino-esp32/releases/download/3.1.1/esp32-3.1.1.zip
  esp32-arduino-libs : https://dl.espressif.cn/github_assets/espressif/esp32-arduino-lib-builder/releases/download/idf-release_v5.3/esp32-arduino-libs-idf-release_v5.3-cfea4f7c-v1.zip
  esp-x32 : https://dl.espressif.cn/github_assets/espressif/crosstool-NG/releases/download/esp-13.2.0_20240530/xtensa-esp-elf-13.2.0_20240530-x86_64-w64-mingw32_hotfix.zip
  xtensa-esp-elf-gdb : https://dl.espressif.cn/github_assets/espressif/binutils-gdb/releases/download/esp-gdb-v14.2_20240403/xtensa-esp-elf-gdb-14.2_20240403-x86_64-w64-mingw32.zip
  esp-rv32 : https://dl.espressif.cn/github_assets/espressif/crosstool-NG/releases/download/esp-13.2.0_20240530/riscv32-esp-elf-13.2.0_20240530-x86_64-w64-mingw32.zip
  riscv32-esp-elf-gdb : https://dl.espressif.cn/github_assets/espressif/binutils-gdb/releases/download/esp-gdb-v14.2_20240403/riscv32-esp-elf-gdb-14.2_20240403-x86_64-w64-mingw32.zip
  openocd-esp32 : https://dl.espressif.cn/github_assets/espressif/openocd-esp32/releases/download/v0.12.0-esp32-20241016/openocd-esp32-win64-0.12.0-esp32-20241016.zip
  esptool_py : https://dl.espressif.cn/github_assets/espressif/arduino-esp32/releases/download/3.1.0-RC3/esptool-v4.9.dev3-win64.zip
  mklittlefs : https://dl.espressif.cn/github_assets/earlephilhower/esp-quick-toolchain/releases/download/3.0.0-gnu12/x86_64-w64-mingw32.mklittlefs-c41e51a.200706.zip

是否开始下载？输入 Y 确认：y
正在下载 esp32-platform ...
esp32-3.1.1.zip               100%[=================================================>]  24.08M  21.2MB/s    in 1.1s
正在下载 esp32-arduino-libs ...
esp32-arduino-libs-idf-releas 100%[=================================================>] 325.32M  34.3MB/s    in 9.3s
正在下载 esp-x32 ...
xtensa-esp-elf-13.2.0_2024053 100%[=================================================>] 257.33M  35.7MB/s    in 8.7s
正在下载 xtensa-esp-elf-gdb ...
xtensa-esp-elf-gdb-14.2_20240 100%[=================================================>]  27.05M  28.4MB/s    in 1.0s
正在下载 esp-rv32 ...
riscv32-esp-elf-13.2.0_202405 100%[=================================================>] 352.69M  30.1MB/s    in 11s
正在下载 riscv32-esp-elf-gdb ...
riscv32-esp-elf-gdb-14.2_2024 100%[=================================================>]  26.65M  24.9MB/s    in 1.1s
正在下载 openocd-esp32 ...
openocd-esp32-win64-0.12.0-es 100%[=================================================>]   2.81M  11.2MB/s    in 0.3s
正在下载 esptool_py ...
esptool-v4.9.dev3-win64.zip   100%[=================================================>]  34.40M  29.2MB/s    in 1.2s
正在下载 mklittlefs ...
x86_64-w64-mingw32.mklittlefs 100%[=================================================>] 337.04K  --.-KB/s    in 0.1s
全部下载完成！
```

如果上面还有问题，可以按照上面的文件名去网上搜索，自行下载。

2、下载完后，重新打开Arduino IDE，点击左侧边栏的 **“开发板管理器”** (图标是几个板子叠加)，搜索框输入 `esp32`。

3、找到由 **Espressif Systems** 提供的 `esp32`，选择版本`3.1.1`（必须是上面离线下载的版本）， 点击 **安装**，这次很快就完成了，因为本地已经存在了。

<img width="1184" height="546" alt="局部截取_20260328_180924" src="https://github.com/user-attachments/assets/631571dd-3910-470c-ac9a-79b8bfb97bf5" />
