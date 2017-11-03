$song_path = $args[0]
$label = $args[1]

## load the assmbly
[Reflection.Assembly]::LoadFrom("taglib-sharp.dll") | out-null

## load mp3 file
$flac = [TagLib.File]::Create($song_path)

$flac.Tag.$label

