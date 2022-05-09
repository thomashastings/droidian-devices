# Asus Zenfone Max Pro M2


**Make a backup now, as your device will be wiped.**


## 0. Download the needed files and tools
- [Droidian `rootfs`](https://github.com/droidian-images/rootfs-api28gsi-all/releases/download/droidian%2Fbullseye%2F22/droidian-rootfs-api28gsi-arm64_20210531.zip) (specific build required)
- [Droidian `devtools`](https://github.com/droidian-images/rootfs-api28gsi-all/releases/download/droidian%2Fbullseye%2F22/droidian-devtools-arm64_20210531.zip) (specific build required)
- [Android 9 (Pie) stock firmware](https://dlcdnets.asus.com/pub/ASUS/ZenFone/ZB631KL/UL-ASUS_X01BD-WW-16.2017.1912.072.999-user.zip)
- [LineageOS 16 (unofficial build)](https://sourceforge.net/projects/kubersharma001/files/X01BD/lineage-16.0/lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download)
- [Latest TWRP recovery](https://dl.twrp.me/X01BD/)
- [Droidian adaptation zip (unofficial)](https://github.com/thomashastings/droidian-x01bd-guide/releases/download/v0.1/x01bd-adaptation_20220508.zip)


## 1. Device preparation
- Save your APN (Android)
    - The `Access Point Name` or `APN` can be found in the Settings menu of Android
    - Take a piece of paper or a text editor, and write down everything that you see on that screen
    - These are likely to include a URL (e. g., `internet.carrier.net`), a username, and possibly a password
- Unlock the bootloader (Computer)
    - Refer to the instructions provided by the device manufacturer
    - Other useful sources include the [LineageOS wiki](https://wiki.lineageos.org/devices/) and [xda-developers](https://www.xda-developers.com/search2/)
- Boot into recovery (Computer)
    - Boot TWRP by running `fastboot boot twrp-VERSION-X01BD.img`
- Wipe the device (TWRP)
    - Go to the `Wipe` menu
    - Select `Advanced wipe`
    - Tick the boxes called `Dalvik / ART cache`, `Cache`, `System`, `Vendor`, `Data`
    - Swipe to Wipe
    - Go back to the previous menu
    - Choose `Format data` and type `yes`
    - Go back to the main menu and select `Reboot`
    - Choose `Bootloader`
    - Boot TWRP again by running `fastboot boot twrp-VERSION-X01BD.img`
- Copy the files to the device  (Computer)
    - When TWRP is booted, open the device's `Internal storage` from your computer
    - Copy all of the files you downloaded to this folder

## 2. Droidian installation (TWRP)
- Install the required base Android version (9, 10, 11)
    - Install the file called `UL-ASUS_X01BD-WW-16.2017.1912.072.999-user.zip` as a Zip file
    - Alternatively, you can enter ADB mode and `sideload UL-ASUS_X01BD-WW-16.2017.1912.072.999-user.zip`
- Install the required LineageOS version
    - Install the file called `lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download`
    - Alternatively, you can enter ADB mode and `sideload lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download`
- Install Recovery
    - Install the file called `twrp-VERSION-X01BD.img` as an Image to the `recovery` partition
- Install Droidian `rootfs`
    - Install the file named `droidian-rootfs-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter ADB mode and sideload the file `droidian-rootfs-arm64_YYYYMMDD.zip`
- Install `devtools` (for stable release)
    - Install the file named `droidian-devtools-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter ADB mode and sideload the file `droidian-devtools-arm64_YYYYMMDD.zip`
    - This component is already included in nightly builds
    - Installation is optional for stable releases, but it is recommended, because it helps with debugging

## 3. Finalizing the installation
- Install adaptation package as a flashable zip (TWRP)
    - Install the file named `x01bd-adaptation_20220508.zip` as a Zip file
    - Alternatively, you can enter ADB mode and sideload the file `x01bd-adaptation_20220508.zip`
- Boot your device
    - Go to the `Reboot` menu and choose `System`
    - TWRP might complain that there is no OS installed, but that's fine
    - The first boot may take longer, and at least one spontaneous reboot is expected during the process
    - You should be greeted with the lock screen, the default password is `1234`

Congratulations, if everything went well, now you should be running Droidian.

## Notes
### Porting status
You can check out the status of the port [here](https://github.com/thomashastings/droidian-x01bd-guide/blob/main/STATUS.md)

### SSH
Flashing the `devtools` zip enables `SSH` over USB. To use it, connect your phone to your computer and type `ssh droidian@10.15.19.82`, the password is `1234` (on Windows, you may need [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/))

### Applications
You can find a list of mobile-friendly Linux applications at [LinuxPhoneApps](https://linuxphoneapps.org/)

## Credit
[aboothahir](https://gitlab.com/iAboothahir)

[kubersharma](https://sourceforge.net/u/kubersharma/profile/)

[bauuuuu](https://forum.xda-developers.com/m/bauuuuu.6410262/)

[Droidian](http://droidian.org/)

[Mobian](https://mobian-project.org/)

[UBports](https://ubuntu-touch.io/)
# Xiaomi Pocophone F1


**Make a backup now, as your device will be wiped.**


## 0. Download the needed files and tools
- [Droidian `rootfs` and `devtools`](https://github.com/droidian-images/rootfs-api28gsi-all/releases) for `arm64` (nightly releases include devtools)
- [Android 9 (Pie) stock firmware](https://xiaomifirmwareupdater.com/download/?file=fw_beryllium_miui_POCOF1Global_9.6.27_6673f8a455_9.0.zip)
- [LineageOS 16 (unofficial build)](https://sourceforge.net/projects/kubersharma001/files/X01BD/lineage-16.0/lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download)
- [Vendor image](https://github.com/ubports-beryllium/artifacts/releases/download/v3/vendor.img)
- [Latest boot image](https://github.com/Unofficial-droidian-for-pocof1/linux_android_xiaomi_beryllium/releases)
- [Latest TWRP recovery](https://dl.twrp.me/beryllium/)
- [Droidian adaptation zip (unofficial)](https://github.com/Unofficial-droidian-for-pocof1/android-recovery-beryllium-adaptation/releases)


## 1. Device preparation
- Save your APN (Android)
    - The `Access Point Name` or `APN` can be found in the Settings menu of Android
    - Take a piece of paper or a text editor, and write down everything that you see on that screen
    - These are likely to include a URL (e. g., `internet.carrier.net`), a username, and possibly a password
- Unlock the bootloader (Computer)
    - Refer to the instructions provided by the device manufacturer
    - Other useful sources include the [LineageOS wiki](https://wiki.lineageos.org/devices/) and [xda-developers](https://www.xda-developers.com/search2/)
- Boot into recovery (Computer)
    - Boot TWRP by running `fastboot boot twrp-VERSION-beryllium.img`
- Wipe the device (TWRP)
    - Go to the `Wipe` menu
    - Select `Advanced wipe`
    - Tick the boxes called `Dalvik / ART cache`, `Cache`, `System`, `Vendor`, `Data`
    - Swipe to Wipe
    - Go back to the previous menu
    - Choose `Format data` and type `yes`
    - Go back to the main menu and select `Reboot`
    - Choose `Bootloader`
    - Boot TWRP again by running `fastboot boot twrp-VERSION-beryllium.img`
- Copy the files to the device  (Computer)
    - When TWRP is booted, open the device's `Internal storage` from your computer
    - Copy all of the files you downloaded to this folder

## 2. Droidian installation (TWRP)
- Install the required base Android version (9, 10, 11)
    - Install the file called `fw_beryllium_miui_POCOF1Global_9.6.27_6673f8a455_9.0.zip` as a Zip file
    - Alternatively, you can enter ADB mode and `sideload fw_beryllium_miui_POCOF1Global_9.6.27_6673f8a455_9.0.zip`
- Install the required LineageOS version
    - Install the file called `lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download`
    - Alternatively, you can enter ADB mode and `sideload lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download`
- Install the vendor image
    - Install the file called `vendor.img` as an Image to the `vendor` partition
    - Alternatively, you can enter fastboot mode and `fastboot flash vendor vendor.img`
- Install the vendor image
    - Install the file called `boot.img` as an Image to the `boot` partition
    - Alternatively, you can enter fastboot mode and `fastboot flash boot boot.img`
- Install Recovery
    - Install the file called `twrp-VERSION-beryllium.img` as an Image to the `recovery` partition
- Install Droidian `rootfs`
    - Install the file named `droidian-rootfs-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter ADB mode and sideload the file `droidian-rootfs-arm64_YYYYMMDD.zip`
- Install `devtools` (for stable release)
    - Install the file named `droidian-devtools-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter ADB mode and sideload the file `droidian-devtools-arm64_YYYYMMDD.zip`
    - This component is already included in nightly builds
    - Installation is optional for stable releases, but it is recommended, because it helps with debugging

## 3. Finalizing the installation
- Install adaptation package as a flashable zip (TWRP)
    - Install the file named `android-recovery-beryllium-adaptation_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter ADB mode and sideload the file `android-recovery-beryllium-adaptation_YYYYMMDD.zip`
- Boot your device
    - Go to the `Reboot` menu and choose `System`
    - TWRP might complain that there is no OS installed, but that's fine
    - The first boot may take longer, and at least one spontaneous reboot is expected during the process
    - You should be greeted with the lock screen, the default password is `1234`

Congratulations, if everything went well, now you should be running Droidian.

## Notes
### SIM slot
Dual-SIM mode is not supported as of now. Only the SIM2 slot is active, so a microSD card can be used at the same time.

### Extras
For other tweaks, open the `King's Cross` terminal app, and run `beryllium-extras.sh`. This includes a notch fix and automated installation of Waydroid.

### SSH
Flashing the `devtools` zip enables `SSH` over USB. To use it, connect your phone to your computer and type `ssh droidian@10.15.19.82`, the password is `1234` (on Windows, you may need [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/))

### Applications
You can find a list of mobile-friendly Linux applications at [LinuxPhoneApps](https://linuxphoneapps.org/)

## Credit
[Joel Selvaraj](https://github.com/joelselvaraj)

[1petro](https://github.com/1petro)

[Droidian](http://droidian.org/)

[Mobian](https://mobian-project.org/)

[UBports](https://ubuntu-touch.io/)
