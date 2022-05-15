import yaml
import os
from schema import Or, Schema, SchemaError
from schema_validation import validate_file

# Check for valid files
devices = []
for file in os.listdir("devices"):
    device = yaml.load(open(f"devices/{file}", 'r'),Loader=yaml.FullLoader)
    if validate_file(device) == True:
        devices.append(device)
    
if devices == []:
    print('No valid device files found, exiting')
    exit()
print()

# Generate markdown as a list of lines
outlines = []
for device in devices:
    print('Generating', device['codename'],"...")
    outlines.append("# "+device['manufacturer']+" "+device['name']+" ("+device['codename']+")")
    outlines.append("**Make a backup now, as your device will be wiped.**")
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
    if device['manufacturer'] == "Xiaomi":
        outlines.append("- A USB 2.0 port/hub with an actual USB 2.0 controller is recommended")
        outlines.append("    - Using `fastboot` on a USB 3.0 port may cause errors with some Xiaomi devices")
    outlines.append("- Save your APN (Android)")
    outlines.append("    - The `Access Point Name` or `APN` can be found in the Settings menu of Android")
    outlines.append("    - Take a piece of paper or a text editor, and write down everything that you see on that screen")
    outlines.append("    - These are likely to include a URL (e. g., `internet.carrier.net`), a username, and possibly a password")
    outlines.append("- Unlock the bootloader (Computer)")
    outlines.append("    - Refer to the instructions provided by the device manufacturer")
    outlines.append("    - Other useful sources include the [LineageOS wiki](https://wiki.lineageos.org/devices/) and [xda-developers](https://www.xda-developers.com/search2/)")
    if device['recovery']['must_flash'] == True:
        outlines.append("- Flash recovery (Computer)")
        outlines.append("    - Flash "+device['recovery']['name']+" to your device by running `fastboot flash recovery "+device['recovery']['filename']+"`")
        outlines.append("    - Boot into recovery by pressing "+device['recovery_mode'])
        outlines.append("    - If your device boots to the stock recovery menu at some point, you should repeat this step.") 
    else:
        outlines.append("- Boot into recovery (Computer)")
        outlines.append("    - Boot "+device['recovery']['name']+" by running `fastboot boot "+device['recovery']['filename']+"`")
    outlines.append("- Wipe the device ("+device['recovery']['name']+")")
    outlines.append("    - Go to the `Wipe` menu")
    outlines.append("    - Select `Advanced wipe`")
    outlines.append("    - Tick the boxes called `Dalvik / ART cache`, `Cache`, `System`, `Vendor`, `Data`")
    outlines.append("    - Swipe to Wipe")
    outlines.append("    - Go back to the previous menu")
    outlines.append("    - Choose `Format data` and type `yes`")
    outlines.append("    - Go back to the main menu and select `Reboot`")
    if device['recovery']['must_flash'] == True:
        outlines.append("    - Choose `Recovery`")       
    else:
        outlines.append("    - Choose `Bootloader`")
        outlines.append("    - Boot "+device['recovery']['name']+" again by running `fastboot boot "+device['recovery']['filename']+"`")
    outlines.append("- Copy the files to the device  (Computer)")
    outlines.append("    - When "+device['recovery']['name']+" is booted, open the device's `Internal storage` from your computer")
    outlines.append("    - Copy all of the files you downloaded to this folder")
    outlines.append("")
    outlines.append("## 2. Droidian installation ("+device['recovery']['name']+")")
    if device['ab_slot'] == True:
        outlines.append("- Install base Android version and/or Vendor to both A/B slots")
        outlines.append("  - Go to the `Reboot` menu and see which slot is active")
        outlines.append("  - If it says `Slot A`, then select `Slot B` to be the active slot, and boot "+device['recovery']['name']+" again")
        outlines.append("")
        outlines.append("- **With `Slot B` as active:**")
        if device['android']['filename'] is not None:
            outlines.append("    - Install the file called `"+device['android']['filename']+"` as a Zip file")
            outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload "+device['android']['filename']+"`")
        if device['vendor_zip']['filename'] is not None:
            outlines.append("    - Install the file called `"+device['vendor_zip']['filename']+"`")
            outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload "+device['vendor_zip']['filename']+"`")
        outlines.append("-    Now switch back to `Slot A` and boot "+device['recovery']['name']+" again (must boot again, switching is not enough)")
        outlines.append("")
        outlines.append("- **With `Slot A` as active:**")
        if device['android']['filename'] is not None:
            outlines.append("    - Install the file called `"+device['android']['filename']+"` as a Zip file")
            outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload "+device['android']['filename']+"`")
        if device['vendor_zip']['filename'] is not None:
            outlines.append("    - Install the file called `"+device['vendor_zip']['filename']+"`")
            outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload "+device['vendor_zip']['filename']+"`")
        outlines.append("    - For the rest of the guide, keep using `Slot A`")
    else:     
        if device['android']['filename'] is not None:
            outlines.append("- Install the required base Android version (9, 10, 11)")
            outlines.append("    - Install the file called `"+device['android']['filename']+"` as a Zip file")
            outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload "+device['android']['filename']+"`")
        if device['vendor_zip']['filename'] is not None:
            outlines.append("- Install the required vendor version")
            outlines.append("    - Install the file called `"+device['vendor_zip']['filename']+"`")
            outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload "+device['vendor_zip']['filename']+"`")
    if device['vendor_image']['filename'] is not None:
        outlines.append("- Install the vendor image")
        outlines.append("    - Install the file called `"+device['vendor_image']['filename']+"` as an Image to the `Vendor` partition")
        outlines.append("    - Alternatively, you can enter fastboot mode and `fastboot flash vendor "+device['vendor_image']['filename']+"`")
    if device['boot']['filename'] is not None:
        outlines.append("- Install the boot image")
        outlines.append("    - Install the file called `"+device['boot']['filename']+"` as an Image to the `Boot` partition")
        outlines.append("    - Alternatively, you can enter fastboot mode and `fastboot flash boot "+device['boot']['filename']+"`")
    if device['recovery']['filename'] is not None and device['recovery']['must_flash'] is not True:
        outlines.append("- Install recovery")
        if device['recovery']['name'] == "TWRP":
            outlines.append("    - Install the file called `"+device['recovery']['filename']+"` as an Image to the `Recovery` partition")
        elif device['recovery']['must_flash'] is not True:
            outlines.append("    - Please, follow the official guide to install "+device['recovery']['name'])
    outlines.append("- Install Droidian `rootfs`")
    outlines.append("    - Install the file named `droidian-rootfs-"+device['arch']+"_YYYYMMDD.zip` as a Zip file")
    outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-rootfs-"+device['arch']+"_YYYYMMDD.zip`")
    outlines.append("- Install `devtools` (for stable release)")
    outlines.append("    - Install the file named `droidian-devtools-"+device['arch']+"_YYYYMMDD.zip` as a Zip file")
    outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload droidian-devtools-"+device['arch']+"_YYYYMMDD.zip`")
    outlines.append("    - This component is already included in nightly builds")
    outlines.append("    - Installation is optional for stable releases, but it is recommended, because it helps with debugging")
    outlines.append("")
    outlines.append("## 3. Finalizing the installation")
    if device['adaptation']['filename'] is not None:
        outlines.append("- Install adaptation package as a flashable zip ("+device['recovery']['name']+")")
        outlines.append("    - Install the file named `"+device['adaptation']['filename']+"` as a Zip file")
        outlines.append("    - Alternatively, you can enter `ADB sideload` mode and run `adb sideload "+device['adaptation']['filename']+"`")
    outlines.append("- Boot your device")
    outlines.append("    - Go to the `Reboot` menu and choose `System`")
    outlines.append("    - "+device['recovery']['name']+" might complain that there is no OS installed, but that's fine")
    outlines.append("    - The first boot may take longer, and at least one spontaneous reboot is expected during the process")
    outlines.append("    - You should be greeted with the lock screen, the default password is `1234`")
    if device['command'] is not None:
        outlines.append("- Run a specific command after first boot (Droidian)")
        outlines.append("    - Open the `King's Cross` application or connect via SSH (see the `SSH` entry in the Notes below), and type in the following:")
        outlines.append("```")
        for line in device['command']:
            outlines.append(line)
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
    outlines.append("")
    if device['contact']['link'] is not None:
        outlines.append("You can ask for assistance specific to this device at ["+device['contact']['text']+"]("+device['contact']['link']+").")
    outlines.append("")
    outlines.append("")

# Output list of lines to the target file
outfile_name = "DETAILED_GUIDES.md"
outfile = open(outfile_name, 'w')
for line in outlines:
    outfile.write(line+'\n')
    #print(line)
outfile.close()
print('Done.')
