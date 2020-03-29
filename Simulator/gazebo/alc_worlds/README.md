# ALC_WORLDS ROS Package
This package is a reduction and refactoring of the Gazebo worlds used in F1 Tenth simulations. World files are taken from [here](https://github.com/mlab-upenn/f110-fall2018-skeletons).

## Testing
Test in a ROS-ready environment with the following command:
```bash
roslaunch test_world.launch <arg>:=<value>...
```
 This will launch a Gazebo instance with the map loaded.

Arguments:
- `world_name`: Folder name containing track you want to launch (default: track_barca)
- `gui`: `true` or `false` to launch Gazebo visually. (default: true)

## Troubleshooting
1. Launching throws an `RLException` and cites `Invalid <arg> tag: alc_worlds`

The `alc_worlds` package wasn't in the ROS path (check with `rospack list`). Fix with:
```bash
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/path/to/alc_worlds
```

2. Gazebo gives an `Unable to find uri` error

Gazebo couldn't load the `model.config` file for the given track, because it wasn't in the Gazebo model path. Fix with:
```bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/path/to/alc_worlds
```
