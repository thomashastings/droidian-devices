# Droidian device support

- A list of supported devices can be found [here](https://github.com/thomashastings/droidian-devices/blob/main/DEVICE_LIST.md)
- This is tool generates guides (GitHub markdown format) for devices supported by Droidian, based on a YAML configuration file.
- The latest version of the devices file is the [`devices.yml`](https://github.com/thomashastings/droidian-devices/blob/main/devices.yml).
- An empty device template is also provided as [`device_template.yml`](https://github.com/thomashastings/droidian-devices/blob/main/device_template.yml).
- The script depends on the `yaml` Python package, you need to install it before using running the script.

## Device parameters explained
These are the parameters used in `devices.yml`. Start each device entry with a `-`.
- `manufacturer`: manufacturer of the device
- `name`: name of the device 
- `codenamename`: codename of the device
- `support`: `official` or `community`
- `device_type`: phone, tablet, etc
- `halium_version`: 9, 10, or 11
- `fastboot_mode`: button combination for booting in fastboot mode
- `recovery_mode`: button combination for booting in recovery mode
- `ab_slot`: `True` if the device has A/B slots, leave empty if not
- `api_version`: version of the android API used for the device
- `arch`: device architecture
- `droidian_release`: a link to the correspodning Droidian release
- `droidian_required_build`: some devices might need a specific build, links to the files can be specified here, otherwise leave emopty
- `android`\*: base android version to install before Droidian
- `vendor_zip`\*: a vendor package to be flashed as zip
- `vendor_image`\*: a vendor image to be flashed as an image
- `boot`\*: Droidian boot image
- `recovery`\*\*: recommended recovery for the device
- `adaptation`\*: adaptation package to be flashed as zip
- `statuspage`: a link to the porting status page of the device, leave empty if there is no page
- `contact`: each contact should start with a `-`, as it becomes a list. `text`: what the text should say, `link`: where the hyperlink should point to
- `credit`: also a list, each entry should start with a `-`. `name`: the name of the maintainer, `link`: maintainer's page
- `command`: a list of commands that need to be run after first boot, start each line of the commands with a `-`
- `notes`: additional considerations for the device, start each note with a `-`. A note contains a `title` entry and a `text` that contains the note itself
- `port_status`: please, see the `device_template.yml` file for details

\* `android`, `vendor_zip`, `vendor_image`, and `boot` have multiple parts. The `link` contains the actual link to the file or release page; the `text` contains the string what the download link should say in the page; and the `filename` specifies the name of the file that identifies the file when flashing.

\*\* `recovery` has two further entry called `name` and `must_flash`. `name` specifies the name of the recovery, e. g., `TWRP` or `Orange Fox Recovery`; if `must_flash` is set to `True`, the user will be prompted to flash the recovery instead of just booting it (some devices have been reported to not support directly booting to the recovery image)
