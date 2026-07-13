; YaSara Professional v1.0 Inno Setup scaffold
#define MyAppName "YaSara Professional"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "YaSara"
#define MyAppExeName "YaSara_Start_Backend.bat"

[Setup]
AppId={{A9F0B6E6-CA29-4E4B-B7B2-YASARA100}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\YaSara Professional
DefaultGroupName={#MyAppName}
OutputDir=..\dist
OutputBaseFilename=YaSara_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "..\backend\*"; DestDir: "{app}\backend"; Flags: recursesubdirs createallsubdirs
Source: "..\docs\*"; DestDir: "{app}\docs"; Flags: recursesubdirs createallsubdirs
Source: "..\windows_runtime\*"; DestDir: "{app}\windows_runtime"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Start YaSara Backend"; Filename: "{app}\windows_runtime\YaSara_Start_Backend.bat"
Name: "{group}\Run YaSara Tests"; Filename: "{app}\windows_runtime\YaSara_Run_Tests.bat"
