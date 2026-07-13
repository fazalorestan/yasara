[Setup]
AppName=YaSara Professional
AppVersion=1.1.0
DefaultDirName={pf}\YaSara Professional
DefaultGroupName=YaSara Professional
OutputDir=D:\yasara_clean\dist
OutputBaseFilename=YaSara_Setup_v1_1
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "D:\yasara_clean\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\YaSara Professional"; Filename: "{app}\windows_runtime\YaSara_Start_Backend.bat"
Name: "{commondesktop}\YaSara Professional"; Filename: "{app}\windows_runtime\YaSara_Start_Backend.bat"