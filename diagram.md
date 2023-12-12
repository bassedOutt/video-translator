@startuml
!define RECTANGLE class

RECTANGLE "Python App\n(using PyTube)" as PyTube
RECTANGLE "Download YouTube Video\nwith Captions" as Download
RECTANGLE "Translate Captions\n(Keep Timestamps)" as Translate
RECTANGLE "Azure Text-to-Speech\n(Convert Captions to Audio)" as AzureTTS
RECTANGLE "Assemble Audio Files\ninto One Track" as AssembleAudio
RECTANGLE "Replace Original Audio\nwith New Track" as ReplaceAudio
RECTANGLE "Generate Final Video\nwith Translated Audio" as FinalVideo

PyTube -down-> Download
Download -right-> Translate
Translate -down-> AzureTTS
AzureTTS -right-> AssembleAudio
AssembleAudio -down-> ReplaceAudio
ReplaceAudio -down-> FinalVideo
@enduml
