# Prepare the request body
$body = @{
    model = "qwen3:0.6b"
    prompt = "hi"
    stream = $false
} | ConvertTo-Json

# Use Invoke-RestMethod to call Ollama API
try {
    $response = Invoke-RestMethod -Uri "http://localhost:11434/api/generate" `
        -Method POST `
        -Body $body `
        -ContentType "application/json"
    
    Write-Output "Response: $($response.response)"
} catch {
    Write-Output "Error: $_"
}
