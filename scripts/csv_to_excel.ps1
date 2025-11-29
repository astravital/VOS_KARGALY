# Script to convert CSV files to Excel
# Uses Excel COM object to create a file with two sheets

param(
    [string]$HmiTagsCsv = "CURSOR_PROJECT\ARM_1\HMI_TAGS\HMI_TAGS.csv",
    [string]$MultiplexingCsv = "CURSOR_PROJECT\ARM_1\HMI_TAGS\multiplexing.csv",
    [string]$OutputExcel = "CURSOR_PROJECT\ARM_1\HMI_TAGS\HMI_TAGS.xlsx"
)

# Get absolute paths
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir

$HmiTagsCsvPath = Join-Path $projectRoot $HmiTagsCsv
$MultiplexingCsvPath = Join-Path $projectRoot $MultiplexingCsv
$OutputExcelPath = Join-Path $projectRoot $OutputExcel

Write-Host "Converting CSV to Excel..."
Write-Host "HMI Tags CSV: $HmiTagsCsvPath"
Write-Host "Multiplexing CSV: $MultiplexingCsvPath"
Write-Host "Output Excel: $OutputExcelPath"

# Check if files exist
if (-not (Test-Path $HmiTagsCsvPath)) {
    Write-Error "File not found: $HmiTagsCsvPath"
    exit 1
}

if (-not (Test-Path $MultiplexingCsvPath)) {
    Write-Error "File not found: $MultiplexingCsvPath"
    exit 1
}

# Create Excel object
$excel = $null
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    
    # Create new workbook
    $workbook = $excel.Workbooks.Add()
    
    # Remove extra sheets (keep only one)
    while ($workbook.Sheets.Count -gt 1) {
        $workbook.Sheets.Item($workbook.Sheets.Count).Delete()
    }
    
    # First sheet - HMI Tags
    $sheet1 = $workbook.Sheets.Item(1)
    $sheet1.Name = "hmi_tags"
    
    # Read CSV and write to sheet
    $hmiTagsContent = Get-Content $HmiTagsCsvPath -Encoding UTF8
    $row = 1
    foreach ($line in $hmiTagsContent) {
        $columns = $line -split ";"
        $col = 1
        foreach ($value in $columns) {
            $sheet1.Cells.Item($row, $col) = $value
            $col++
        }
        $row++
    }
    Write-Host "Written $($row - 1) rows to sheet 'hmi_tags'"
    
    # Add second sheet - Multiplexing
    $sheet2 = $workbook.Sheets.Add([System.Reflection.Missing]::Value, $sheet1)
    $sheet2.Name = "multiplexing"
    
    # Read CSV and write to sheet
    $multiplexingContent = Get-Content $MultiplexingCsvPath -Encoding UTF8
    $row = 1
    foreach ($line in $multiplexingContent) {
        $columns = $line -split ";"
        $col = 1
        foreach ($value in $columns) {
            $sheet2.Cells.Item($row, $col) = $value
            $col++
        }
        $row++
    }
    Write-Host "Written $($row - 1) rows to sheet 'multiplexing'"
    
    # Delete existing file if exists
    if (Test-Path $OutputExcelPath) {
        Remove-Item $OutputExcelPath -Force
    }
    
    # Save file
    $workbook.SaveAs($OutputExcelPath, 51) # 51 = xlOpenXMLWorkbook (.xlsx)
    Write-Host "Excel file saved: $OutputExcelPath"
    
    # Close Excel
    $workbook.Close($false)
    $excel.Quit()
    
    # Release COM objects
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($sheet2) | Out-Null
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($sheet1) | Out-Null
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($workbook) | Out-Null
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
    
    Write-Host "Conversion completed successfully!"
}
catch {
    Write-Error "Error during conversion: $($_.Exception.Message)"
    if ($excel) {
        $excel.Quit()
        [System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
    }
    exit 1
}
