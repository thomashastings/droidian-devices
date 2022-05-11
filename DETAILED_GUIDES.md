# Xiaomi Pocophone F1 (beryllium)
**Make a backup now, as your device will be wiped.**
## 0. Download the needed files and tools
- [Droidian `rootfs` and `devtools`](https://github.com/droidian-images/rootfs-api28gsi-all/releases) for `arm64` (nightly releases include devtools)
- [Android 9 (Pie) stock firmware](https://xiaomifirmwareupdater.com/download/?file=fw_beryllium_miui_POCOF1Global_9.6.27_6673f8a455_9.0.zip)
- [Vendor image](https://github.com/ubports-beryllium/artifacts/releases/download/v3/vendor_image.img)
- [Latest boot image](https://github.com/Unofficial-droidian-for-pocof1/linux_android_xiaomi_beryllium/releases)
- [Latest TWRP recovery](https://dl.twrp.me/beryllium/)
- [Adaptation (unofficial)](https://github.com/Unofficial-droidian-for-pocof1/android-recovery-beryllium-adaptation/releases)


## 1. Device preparation
- A USB 2.0 port/hub with an actual USB 2.0 controller is recommended
    - Using `fastboot` on a USB 3.0 port may cause errors with some Xiaomi devices
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
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload fw_beryllium_miui_POCOF1Global_9.6.27_6673f8a455_9.0.zip`
- Install the vendor image
    - Install the file called `vendor.img` as an Image to the `Vendor` partition
    - Alternatively, you can enter fastboot mode and `fastboot flash vendor vendor.img`
- Install the boot image
    - Install the file called `boot.img` as an Image to the `Boot` partition
    - Alternatively, you can enter fastboot mode and `fastboot flash boot boot.img`
- Install recovery
    - Install the file called `twrp-VERSION-beryllium.img` as an Image to the `Recovery` partition
- Install Droidian `rootfs`
    - Install the file named `droidian-rootfs-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-rootfs-arm64_YYYYMMDD.zip`
- Install `devtools` (for stable release)
    - Install the file named `droidian-devtools-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-devtools-arm64_YYYYMMDD.zip`
    - This component is already included in nightly builds
    - Installation is optional for stable releases, but it is recommended, because it helps with debugging

## 3. Finalizing the installation
- Install adaptation package as a flashable zip (TWRP)
    - Install the file named `android-recovery-beryllium-adaptation_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload android-recovery-beryllium-adaptation_YYYYMMDD.zip`
- Boot your device
    - Go to the `Reboot` menu and choose `System`
    - TWRP might complain that there is no OS installed, but that's fine
    - The first boot may take longer, and at least one spontaneous reboot is expected during the process
    - You should be greeted with the lock screen, the default password is `1234`
- Run a specific command after first boot (Droidian)
    - Open the `King's Cross` application or connect via SSH (see the `SSH` entry in the Notes below), and type in the following:
```
sudo systemctl enable enable-ipa
sudo systemctl reboot
```

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

You can ask for assistance specific to this device at [Droidian for Poco F1 Telegram Group](https://t.me/pocof1droidian).


# Xiaomi Mi 6X (wayne)
**Make a backup now, as your device will be wiped.**
## 0. Download the needed files and tools
- [Droidian `rootfs` and `devtools`](https://github.com/droidian-images/rootfs-api28gsi-all/releases) for `arm64` (nightly releases include devtools)
- [Android 9 Pie Firmware](https://github.com/ubports-xiaomi-sdm660/artifacts/releases/download/v0.1/jasmine_sprout_stock_android9.zip)
- [Vendor (has arb4 firmware!)](https://github.com/TryHardDood/mi-vendor_image-updater/releases/download/wayne-stable/fw-vendor_image_wayne_miui_MI6X_V11.0.6.0.PDCCNXM_f049df201b_9.0.zip)
- [Latest TWRP image](https://dl.twrp.me/wayne/)
- [Latest adaptation zip](https://github.com/Droidian-Mi-A2-6X/adaptation-xiaomi-wayne/releases)


## 1. Device preparation
- A USB 2.0 port/hub with an actual USB 2.0 controller is recommended
    - Using `fastboot` on a USB 3.0 port may cause errors with some Xiaomi devices
- Save your APN (Android)
    - The `Access Point Name` or `APN` can be found in the Settings menu of Android
    - Take a piece of paper or a text editor, and write down everything that you see on that screen
    - These are likely to include a URL (e. g., `internet.carrier.net`), a username, and possibly a password
- Unlock the bootloader (Computer)
    - Refer to the instructions provided by the device manufacturer
    - Other useful sources include the [LineageOS wiki](https://wiki.lineageos.org/devices/) and [xda-developers](https://www.xda-developers.com/search2/)
- Boot into recovery (Computer)
    - Boot TWRP by running `fastboot boot twrp-VERSION-wayne.img`
- Wipe the device (TWRP)
    - Go to the `Wipe` menu
    - Select `Advanced wipe`
    - Tick the boxes called `Dalvik / ART cache`, `Cache`, `System`, `Vendor`, `Data`
    - Swipe to Wipe
    - Go back to the previous menu
    - Choose `Format data` and type `yes`
    - Go back to the main menu and select `Reboot`
    - Choose `Bootloader`
    - Boot TWRP again by running `fastboot boot twrp-VERSION-wayne.img`
- Copy the files to the device  (Computer)
    - When TWRP is booted, open the device's `Internal storage` from your computer
    - Copy all of the files you downloaded to this folder

## 2. Droidian installation (TWRP)
- Install the required base Android version (9, 10, 11)
    - Install the file called `jasmine_sprout_stock_android9.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload jasmine_sprout_stock_android9.zip`
- Install the required vendor version
    - Install the file called `fw-vendor_image_wayne_miui_MI6X_V11.0.6.0.PDCCNXM_f049df201b_9.0.zip`
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload fw-vendor_image_wayne_miui_MI6X_V11.0.6.0.PDCCNXM_f049df201b_9.0.zip`
- Install recovery
    - Install the file called `twrp-VERSION-wayne.img` as an Image to the `Recovery` partition
- Install Droidian `rootfs`
    - Install the file named `droidian-rootfs-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-rootfs-arm64_YYYYMMDD.zip`
- Install `devtools` (for stable release)
    - Install the file named `droidian-devtools-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-devtools-arm64_YYYYMMDD.zip`
    - This component is already included in nightly builds
    - Installation is optional for stable releases, but it is recommended, because it helps with debugging

## 3. Finalizing the installation
- Install adaptation package as a flashable zip (TWRP)
    - Install the file named `droidian-adaptation-xiaomi-wayne-arm64_MMMMDDYY.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-adaptation-xiaomi-wayne-arm64_MMMMDDYY.zip`
- Boot your device
    - Go to the `Reboot` menu and choose `System`
    - TWRP might complain that there is no OS installed, but that's fine
    - The first boot may take longer, and at least one spontaneous reboot is expected during the process
    - You should be greeted with the lock screen, the default password is `1234`

Congratulations, if everything went well, now you should be running Droidian.

## Notes
### Porting status
You can check out the status of the port [here](https://github.com/orgs/Droidian-Mi-A2-6X/projects/1)

### SSH
Flashing the `devtools` zip enables `SSH` over USB. To use it, connect your phone to your computer and type `ssh droidian@10.15.19.82`, the password is `1234` (on Windows, you may need [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/))

### Applications
You can find a list of mobile-friendly Linux applications at [LinuxPhoneApps](https://linuxphoneapps.org/)

## Credit
[kisekinopureya](https://github.com/kisekinopureya)

[Shouko](https://xn--n8ja0d4b0j7a.xn--q9jyb4c/)

[Droidian](http://droidian.org/)

[Mobian](https://mobian-project.org/)

[UBports](https://ubuntu-touch.io/)

You can ask for assistance specific to this device at [Shouko's Lab Telegram Group](https://t.me/shoukolab).


# Xiaomi Redmo Note 7 Pro (violet)
**Make a backup now, as your device will be wiped.**
## 0. Download the needed files and tools
- [Droidian `rootfs` and `devtools`](https://github.com/droidian-images/rootfs-api28gsi-all/releases) for `arch64` (nightly releases include devtools)
- [Android 9 Pie Firmware](https://xiaomifirmwareupdater.com/firmware/violet/weekly/9.9.3/)
- [Android 9 vendor](https://github.com/ubuntu-touch-violet/ubuntu-touch-violet/releases/tag/20210510)
- [Halium-boot](https://gitlab.com/mathew-dennis/xiaomi-violet/-/jobs/2428049402/artifacts/file/out/boot.img)
- [Latest Orange Fox Recovery](https://orangefox.download/device/violet)
- [Adaptation (unofficial)](https://github.com/mathew-dennis/droidian-recovery-flashing-adaptation-violet/releases/tag/v1.1)


## 1. Device preparation
- A USB 2.0 port/hub with an actual USB 2.0 controller is recommended
    - Using `fastboot` on a USB 3.0 port may cause errors with some Xiaomi devices
- Save your APN (Android)
    - The `Access Point Name` or `APN` can be found in the Settings menu of Android
    - Take a piece of paper or a text editor, and write down everything that you see on that screen
    - These are likely to include a URL (e. g., `internet.carrier.net`), a username, and possibly a password
- Unlock the bootloader (Computer)
    - Refer to the instructions provided by the device manufacturer
    - Other useful sources include the [LineageOS wiki](https://wiki.lineageos.org/devices/) and [xda-developers](https://www.xda-developers.com/search2/)
- Flash recovery (Computer)
    - Flash Orange Fox Recovery to your device by running `fastboot flash recovery OrangeFox-violet-stable@VERSION.zip`
    - Boot into recovery by pressing `Vol+` and `Power`
    - If your device boots to the stock recovery menu at some point, you should repeat this step.
- Wipe the device (Orange Fox Recovery)
    - Go to the `Wipe` menu
    - Select `Advanced wipe`
    - Tick the boxes called `Dalvik / ART cache`, `Cache`, `System`, `Vendor`, `Data`
    - Swipe to Wipe
    - Go back to the previous menu
    - Choose `Format data` and type `yes`
    - Go back to the main menu and select `Reboot`
    - Choose `Recovery`
- Copy the files to the device  (Computer)
    - When Orange Fox Recovery is booted, open the device's `Internal storage` from your computer
    - Copy all of the files you downloaded to this folder

## 2. Droidian installation (Orange Fox Recovery)
- Install the required base Android version (9, 10, 11)
    - Install the file called `fw_violet_miui_VIOLET_9.9.3_79d3ccd33b_9.0.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload fw_violet_miui_VIOLET_9.9.3_79d3ccd33b_9.0.zip`
- Install the required vendor version
    - Install the file called `vendor.zip`
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload vendor.zip`
- Install the boot image
    - Install the file called `boot.img` as an Image to the `Boot` partition
    - Alternatively, you can enter fastboot mode and `fastboot flash boot boot.img`
- Install Droidian `rootfs`
    - Install the file named `droidian-rootfs-arch64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-rootfs-arch64_YYYYMMDD.zip`
- Install `devtools` (for stable release)
    - Install the file named `droidian-devtools-arch64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-devtools-arch64_YYYYMMDD.zip`
    - This component is already included in nightly builds
    - Installation is optional for stable releases, but it is recommended, because it helps with debugging

## 3. Finalizing the installation
- Install adaptation package as a flashable zip (Orange Fox Recovery)
    - Install the file named `droidian-recovery-flashing-adaptation-violet.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-recovery-flashing-adaptation-violet.zip`
- Boot your device
    - Go to the `Reboot` menu and choose `System`
    - Orange Fox Recovery might complain that there is no OS installed, but that's fine
    - The first boot may take longer, and at least one spontaneous reboot is expected during the process
    - You should be greeted with the lock screen, the default password is `1234`

Congratulations, if everything went well, now you should be running Droidian.

## Notes
### SSH
Flashing the `devtools` zip enables `SSH` over USB. To use it, connect your phone to your computer and type `ssh droidian@10.15.19.82`, the password is `1234` (on Windows, you may need [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/))

### Applications
You can find a list of mobile-friendly Linux applications at [LinuxPhoneApps](https://linuxphoneapps.org/)

## Credit
[mathew-dennis](https://gitlab.com/mathew-dennis)

[mardy](https://forums.ubports.com/user/mardy)

[Droidian](http://droidian.org/)

[Mobian](https://mobian-project.org/)

[UBports](https://ubuntu-touch.io/)



# Xiaomi Mi A2 (jasmine)
**Make a backup now, as your device will be wiped.**
## 0. Download the needed files and tools
- [Droidian `rootfs` and `devtools`](https://github.com/droidian-images/rootfs-api28gsi-all/releases) for `arm64` (nightly releases include devtools)
- [Android 9 Pie Firmware](https://github.com/ubports-xiaomi-sdm660/artifacts/releases/download/v0.1/jasmine_sprout_stock_android9.zip)
- [Latest TWRP image](https://dl.twrp.me/jasmine_sprout/)
- [Adaptation (unofficial)](https://github.com/thomashastings/droidian-recovery-adaptation-jasmine/releases)


## 1. Device preparation
- A USB 2.0 port/hub with an actual USB 2.0 controller is recommended
    - Using `fastboot` on a USB 3.0 port may cause errors with some Xiaomi devices
- Save your APN (Android)
    - The `Access Point Name` or `APN` can be found in the Settings menu of Android
    - Take a piece of paper or a text editor, and write down everything that you see on that screen
    - These are likely to include a URL (e. g., `internet.carrier.net`), a username, and possibly a password
- Unlock the bootloader (Computer)
    - Refer to the instructions provided by the device manufacturer
    - Other useful sources include the [LineageOS wiki](https://wiki.lineageos.org/devices/) and [xda-developers](https://www.xda-developers.com/search2/)
- Boot into recovery (Computer)
    - Boot TWRP by running `fastboot boot twrp-VERSION-jasmine_sprout.img`
- Wipe the device (TWRP)
    - Go to the `Wipe` menu
    - Select `Advanced wipe`
    - Tick the boxes called `Dalvik / ART cache`, `Cache`, `System`, `Vendor`, `Data`
    - Swipe to Wipe
    - Go back to the previous menu
    - Choose `Format data` and type `yes`
    - Go back to the main menu and select `Reboot`
    - Choose `Bootloader`
    - Boot TWRP again by running `fastboot boot twrp-VERSION-jasmine_sprout.img`
- Copy the files to the device  (Computer)
    - When TWRP is booted, open the device's `Internal storage` from your computer
    - Copy all of the files you downloaded to this folder

## 2. Droidian installation (TWRP)
- Install base Android version and/or Vendor to both A/B slots
  - Go to the `Reboot` menu and see which slot is active
  - If it says `Slot A`, then select `Slot B` to be the active slot, and boot TWRP again

- **With `Slot B` as active:**
    - Install the file called `jasmine_sprout_stock_android9.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload jasmine_sprout_stock_android9.zip`
-    Now switch back to `Slot A` and boot TWRP again (must boot again, switching is not enough)

- **With `Slot A` as active:**
    - Install the file called `jasmine_sprout_stock_android9.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload jasmine_sprout_stock_android9.zip`
    - For the rest of the guide, keep using `Slot A`
- Install recovery
    - Install the file called `twrp-VERSION-jasmine_sprout.img` as an Image to the `Recovery` partition
- Install Droidian `rootfs`
    - Install the file named `droidian-rootfs-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-rootfs-arm64_YYYYMMDD.zip`
- Install `devtools` (for stable release)
    - Install the file named `droidian-devtools-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-devtools-arm64_YYYYMMDD.zip`
    - This component is already included in nightly builds
    - Installation is optional for stable releases, but it is recommended, because it helps with debugging

## 3. Finalizing the installation
- Install adaptation package as a flashable zip (TWRP)
    - Install the file named `jasmine-adaptation_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload jasmine-adaptation_YYYYMMDD.zip`
- Boot your device
    - Go to the `Reboot` menu and choose `System`
    - TWRP might complain that there is no OS installed, but that's fine
    - The first boot may take longer, and at least one spontaneous reboot is expected during the process
    - You should be greeted with the lock screen, the default password is `1234`

Congratulations, if everything went well, now you should be running Droidian.

## Notes
### Porting status
You can check out the status of the port [here](https://github.com/orgs/Droidian-Mi-A2-6X/projects/1)

### SSH
Flashing the `devtools` zip enables `SSH` over USB. To use it, connect your phone to your computer and type `ssh droidian@10.15.19.82`, the password is `1234` (on Windows, you may need [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/))

### Applications
You can find a list of mobile-friendly Linux applications at [LinuxPhoneApps](https://linuxphoneapps.org/)

## Credit
[Shouko](https://いらっしゃい.みんな/)

[kisekinopureya](https://github.com/kisekinopureya)

[Droidian](http://droidian.org/)

[Mobian](https://mobian-project.org/)

[UBports](https://ubuntu-touch.io/)

You can ask for assistance specific to this device at [Shouko's Lab Telegram Group](https://t.me/shoukolab).


# Asus Zenfone Max Pro M2 (EXPERIMENTAL) (X01BD)
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
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload UL-ASUS_X01BD-WW-16.2017.1912.072.999-user.zip`
- Install the required vendor version
    - Install the file called `lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download`
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload lineage-16.0-20191119-UNOFFICIAL-X01BD.zip/download`
- Install recovery
    - Install the file called `twrp-VERSION-X01BD.img` as an Image to the `Recovery` partition
- Install Droidian `rootfs`
    - Install the file named `droidian-rootfs-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-rootfs-arm64_YYYYMMDD.zip`
- Install `devtools` (for stable release)
    - Install the file named `droidian-devtools-arm64_YYYYMMDD.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-devtools-arm64_YYYYMMDD.zip`
    - This component is already included in nightly builds
    - Installation is optional for stable releases, but it is recommended, because it helps with debugging

## 3. Finalizing the installation
- Install adaptation package as a flashable zip (TWRP)
    - Install the file named `x01bd-adaptation_20220508.zip` as a Zip file
    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload x01bd-adaptation_20220508.zip`
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
[thomashastings](https://github.com/thomashastings)

[aboothahir](https://gitlab.com/iAboothahir)

[kubersharma](https://sourceforge.net/u/kubersharma/profile/)

[bauuuuu](https://forum.xda-developers.com/m/bauuuuu.6410262/)

[Droidian](http://droidian.org/)

[Mobian](https://mobian-project.org/)

[UBports](https://ubuntu-touch.io/)


