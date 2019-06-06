#!/bin/sh

# Remove the current dock settings on apple computer located in preferences and replaced with the 
# old saved one..(Doesn't work all the time, have to rerun script 2+ times to work at times).
rm ~/Library/Preferences/com.apple.dock.plist
cp Dock_Setting/com.apple.dock.plist ~/Library/Preferences/
killall Dock

# Set the background to my own background picture in the setting page using AppleScript from shell (change username path to yours!)
osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/nfs/2018/s/szheng/setting/Desktop_Image/abc.jpg"'

# kill 82248
open /Applications/System\ Preferences.app/Contents/MacOS/System\ Preferences
