@startuml
start

:Initialize Python App using PyTube;

:Download YouTube Video with Captions;

:Translate Captions\n(Keep Original Timestamps);

:Convert Translated Captions to Audio\n(using Azure Text-to-Speech);

:Assemble Translated Audio Files\ninto One Track;

:Replace Original Video Audio\nwith New Translated Audio;

:Generate Final Video\nwith Translated Audio;

stop
@enduml
