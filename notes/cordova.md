
Vidéo

#1
Apache Cordova (anciennement Apache Callback ou PhoneGap) est un framework open-source développé par la Fondation Apache.
Il permet de créer des applications pour différentes plateformes en HTML, CSS et JavaScript.
Installation : Java JDK + Android SDK + Apache ANT

```bash
sudo pacman -S jdk8-openjdk ant  # jdk installe jre aussi
sudo npm install -g cordova
cordova --version
java -h
ant -version
cordova create DOSSIER fr.domaine.app "Le nom de mon application"
cordova platforms add android
pikaur -S android-sdk android-sdk-build-tools
sudo pacman -S android-tools gradle

export ANDROID_HOME=/opt/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

```
