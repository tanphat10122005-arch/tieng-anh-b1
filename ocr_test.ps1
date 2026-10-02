[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null

$path = (Resolve-Path "page_18.png").Path
$file = [Windows.Storage.StorageFile]::GetFileFromPathAsync($path).GetAwaiter().GetResult()
$stream = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read).GetAwaiter().GetResult()
$decoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream).GetAwaiter().GetResult()
$bmp = $decoder.GetSoftwareBitmapAsync().GetAwaiter().GetResult()
$lang = [Windows.Globalization.Language]::new("en-US")
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)
$ocrResult = $engine.RecognizeAsync($bmp).GetAwaiter().GetResult()

Write-Output "OCR SUCCESS! Text length: $($ocrResult.Text.Length)"
Write-Output $ocrResult.Text.Substring(0, [Math]::Min(500, $ocrResult.Text.Length))
