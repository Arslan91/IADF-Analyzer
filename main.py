import os, shutil
from subprocess import *
from manifestReader import manifest_reader
from appData import app_data

cwd = os.getcwd()

# creating directories
for root, dir, files in os.walk(cwd + '/apps'):
    for name in files:
        if not os.path.isdir(f'./apps_reversed/{name}') and not name.startswith('.'):
            os.mkdir(f'./apps_reversed/{name}')

        if not os.path.isdir(f'./apps_manifest/{name}') and not name.startswith('.'):
            os.mkdir(f'./apps_manifest/{name}')

        if not os.path.isdir(f'./output') and not name.startswith('.'):
            os.mkdir(f'./output')

        print(f'Extracting APK: {name}\n')
        appName = name.replace('.apk', '')
        p0 = Popen(
            f'unzip -u ./apps/{name} -d ./apps_reversed/{appName}',
            shell=True
        )
        p0.wait()

        print(f'Extracting Android Manifest: {name}\n')
        p1 = Popen(
            f'java -jar ./tools/apktool.jar d ./apps/{name} -o ./apps_manifest/{name}/ -f',
            shell=True
        )
        p1.wait()

# Reversing APKs
apps_reversed = cwd+'/apps_reversed/'
for dirs, subdirs, files in os.walk(apps_reversed):
    for file in files:
        file_path = os.path.join(dirs, file)
        if os.path.isfile(file_path):
            if file_path.endswith('.dex'):
                dir_name = dirs.split('/')
                p2 = Popen(
                    f'./tools/dex2jar/d2j-dex2jar.sh {file_path} -o ./decompiled_apps/{dir_name[-1]}.jar -f',
                    shell=True
                )
                p2.wait()

apps_reversed = cwd+'/apps_reversed/'
for dirs, subdirs, files in os.walk(apps_reversed):
    for d in subdirs:
        shutil.rmtree(os.path.join(dirs, d))

decompiledApps = cwd + '/decompiled_apps'
for dirs, subdirs, files in os.walk(decompiledApps):
    for f in files:
        f_name = f.replace('.jar', '')
        if f.endswith('.jar') and not f.startswith('.'):
            print(f'Decompiling: {f}')
            p3 = Popen(
                f'java -jar ./tools/decompiler.jar -jar ./decompiled_apps/{f} -o ./decompiled_apps/{f_name}',
                shell=True
            )
            p3.wait()
            pass

# Extracting Manifest data
apps_manifest = cwd + '/apps_manifest/'
for dirs, subdirs, files in os.walk(apps_manifest):
    for file in files:
        file_path = os.path.join(dirs, file)
        if os.path.isfile(file_path):
            if file_path.endswith('AndroidManifest.xml'):
                dir_name = dirs.split('/')
                directory = dir_name[-1].replace('.apk', '')

                p4 = Popen(
                    f'mv {file_path} ./decompiled_apps/{directory}.xml',
                    shell=True
                )
                p4.wait()

# Extracting APKs intents data
decompiledApps = cwd + '/decompiled_apps'
for dirs, subdirs, files in os.walk(decompiledApps):
    for manifest in files:
        # if not 'original.xml':
        if manifest.endswith('.xml'):
            if 'original.xml' in manifest:
                pass
            else:
                pass
                manifest_reader(manifest)

        if manifest.endswith('.java'):
            path = os.path.join(dirs, manifest)
            print(f'Extracting Features from {path}')
            app_data(path)
