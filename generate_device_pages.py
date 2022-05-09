import yaml
import os

if os.path.isfile('devices.yml'):
        devices = yaml.load(open('devices.yml', 'r'),Loader=yaml.FullLoader)
else:
    print('No devices.yml found, exiting')
    exit()

print(devices)
print()

outlines = []
for device in devices:
    print('Generating', device['codename'],"...")
    outlines.append("# "+device['manufacturer']+' '+device['name'])
    outlines.append("\n")
    outlines.append("**Make a backup now, as your device will be wiped.**")
    outlines.append("\n")
    outlines.append("## 0. Download the needed files and tools")
    if device['droidian_required_build'] == None or device['droidian_required_build']['rootfs_link'] == None:
        outlines.append("- [Droidian `rootfs` and `devtools`]("+device['droidian_release']+") for `"+device['arch']+"` (nightly releases include devtools)")
    else:
        outlines.append("- [Droidian `rootfs`]("+device['droidian_required_build']['rootfs_link']+") (specific build required)")
        outlines.append("- [Droidian `devtools`]("+device['droidian_required_build']['devtools_link']+") (specific build required)")
    for downloadable in ["android", "vendor_zip", "vendor_image", "boot", "recovery", "adaptation"]:
        if device[downloadable]["link"] is not None:
                outlines.append("- ["+device[downloadable]['text']+"]("+device[downloadable]['link']+")")
    outlines.append("")
    outlines.append("")
    outlines.append("## 1. Device preparation")
    outlines.append("- Save your APN (Android)")
    outlines.append("    - The `Access Point Name` or `APN` can be found in the Settings menu of Android")
    outlines.append("    - Take a piece of paper or a text editor, and write down everything that you see on that screen")
    outlines.append("    - These are likely to include a URL (e. g., `internet.carrier.net`), a username, and possibly a password")
    outlines.append("- Unlock the bootloader (Computer)")
    outlines.append("    - Refer to the instructions provided by the device manufacturer")
    outlines.append("    - Other useful sources include the [vendor_zip wiki](https://wiki.vendor_zip.org/devices/) and [xda-developers](https://www.xda-developers.com/search2/)")
    outlines.append("- Boot into recovery (Computer)")
    outlines.append("    - Boot "+device['recovery']['name']+" by running `fastboot boot "+device['recovery']['filename']+"`")
    outlines.append("- Wipe the device ("+device['recovery']['name']+")")
    outlines.append("    - Go to the `Wipe` menu")
    outlines.append("    - Select `Advanced wipe`")
    outlines.append("    - Tick the boxes called `Dalvik / ART cache`, `Cache`, `System`, `vendor_image`, `Data`")
    outlines.append("    - Swipe to Wipe")
    outlines.append("    - Go back to the previous menu")
    outlines.append("    - Choose `Format data` and type `yes`")
    outlines.append("    - Go back to the main menu and select `Reboot`")
    outlines.append("    - Choose `Bootloader`")
    outlines.append("    - Boot "+device['recovery']['name']+" again by running `fastboot boot "+device['recovery']['filename']+"`")
    outlines.append("- Copy the files to the device  (Computer)")
    outlines.append("    - When "+device['recovery']['name']+" is booted, open the device's `Internal storage` from your computer")
    outlines.append("    - Copy all of the files you downloaded to this folder")
    outlines.append("")
    outlines.append("## 2. Droidian installation ("+device['recovery']['name']+")")
    if device['android']['filename'] is not None:
        outlines.append("- Install the required base Android version (9, 10, 11)")
        outlines.append("    - Install the file called `"+device['android']['filename']+"` as a Zip file")
        outlines.append("    - Alternatively, you can enter ADB mode and `sideload "+device['android']['filename']+"`")
    if device['vendor_zip']['filename'] is not None:
        outlines.append("- Install the required vendor_zip version")
        outlines.append("    - Install the file called `"+device['vendor_zip']['filename']+"`")
        outlines.append("    - Alternatively, you can enter ADB mode and `sideload "+device['vendor_zip']['filename']+"`")
    if device['vendor_image']['filename'] is not None:
        outlines.append("- Install the vendor_image image")
        outlines.append("    - Install the file called `"+device['vendor_image']['filename']+"` as an Image to the `vendor_image` partition")
        outlines.append("    - Alternatively, you can enter fastboot mode and `fastboot flash vendor_image "+device['vendor_image']['filename']+"`")
    if device['boot']['filename'] is not None:
        outlines.append("- Install the vendor_image image")
        outlines.append("    - Install the file called `"+device['boot']['filename']+"` as an Image to the `boot` partition")
        outlines.append("    - Alternatively, you can enter fastboot mode and `fastboot flash boot "+device['boot']['filename']+"`")
    if device['recovery']['filename'] is not None:
        outlines.append("- Install Recovery")
        if device['recovery']['name'] == "TWRP":
            outlines.append("    - Install the file called `"+device['recovery']['filename']+"` as an Image to the `recovery` partition")
        else:
            outlines.append("    - Please, follow the official guide to install "+device['recovery']['name'])
    outlines.append("- Install Droidian `rootfs`")
    outlines.append("    - Install the file named `droidian-rootfs-"+device['arch']+"_YYYYMMDD.zip` as a Zip file")
    outlines.append("    - Alternatively, you can enter ADB mode and sideload the file `droidian-rootfs-"+device['arch']+"_YYYYMMDD.zip`")
    outlines.append("- Install `devtools` (for stable release)")
    outlines.append("    - Install the file named `droidian-devtools-"+device['arch']+"_YYYYMMDD.zip` as a Zip file")
    outlines.append("    - Alternatively, you can enter ADB mode and sideload the file `droidian-devtools-"+device['arch']+"_YYYYMMDD.zip`")
    outlines.append("    - This component is already included in nightly builds")
    outlines.append("    - Installation is optional for stable releases, but it is recommended, because it helps with debugging")
    outlines.append("")
    outlines.append("## 3. Finalizing the installation")
    if device['adaptation']['filename'] is not None:
        outlines.append("- Install adaptation package as a flashable zip ("+device['recovery']['name']+")")
        outlines.append("    - Install the file named `"+device['adaptation']['filename']+"` as a Zip file")
        outlines.append("    - Alternatively, you can enter ADB mode and sideload the file `"+device['adaptation']['filename']+"`")
    outlines.append("- Boot your device")
    outlines.append("    - Go to the `Reboot` menu and choose `System`")
    outlines.append("    - "+device['recovery']['name']+" might complain that there is no OS installed, but that's fine")
    outlines.append("    - The first boot may take longer, and at least one spontaneous reboot is expected during the process")
    outlines.append("    - You should be greeted with the lock screen, the default password is `1234`")
    if device['command'] is not None:
        outlines.append("- Run a specific command after first boot (Droidian)")
        outlines.append("    - Open the `King's Cross` application, and type in the following:")
        outlines.append("```")
        for line in device['command']:
            outlines.append(line)
            outlines.append("")
        outlines.append("```")
    outlines.append("")    
    outlines.append("Congratulations, if everything went well, now you should be running Droidian.")
    outlines.append("")
    outlines.append("## Notes")
    if device['notes'] is not None:
        for note in device['notes']:
            outlines.append("### "+note['title'])
            outlines.append(note['text'])
            outlines.append("")
    if device['statuspage'] is not None:
        outlines.append("### Porting status")
        outlines.append("You can check out the status of the port [here]("+device['statuspage']+")")
        outlines.append("")
    outlines.append("### SSH")
    outlines.append("Flashing the `devtools` zip enables `SSH` over USB. To use it, connect your phone to your computer and type `ssh droidian@10.15.19.82`, the password is `1234` (on Windows, you may need [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/))")
    outlines.append("")
    outlines.append("### Applications")
    outlines.append("You can find a list of mobile-friendly Linux applications at [LinuxPhoneApps](https://linuxphoneapps.org/)")
    outlines.append("")
    outlines.append("## Credit")
    for credit in device['credit']:
        outlines.append("["+credit['name']+"]("+credit['link']+")")
        outlines.append("")
    outlines.append("[Droidian](http://droidian.org/)")
    outlines.append("")
    outlines.append("[Mobian](https://mobian-project.org/)")
    outlines.append("")
    outlines.append("[UBports](https://ubuntu-touch.io/)")

outfile_name = "DETAILED_GUIDES.md"
outfile = open(outfile_name, 'w')
for line in outlines:
    outfile.write(line+'\n')
    print(line)
outfile.close()
