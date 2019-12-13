Option Explicit


Sub testing()

Dim i As Long
Dim OpenPrice As Double
Dim ClosingPrice As Double
Dim Rowprint As Long
Dim YearlyChange As Double
Dim PercentChange As Double
Dim Volume As Double
Dim ws As Worksheet
Dim OpenRow As Long
Dim CloseRow As Long
Dim RowRange As String

ActiveWorkbook.Worksheets(1).Activate

    For Each ws In Worksheets
    ws.Activate

        Range("I1").Value = "Ticker"
        Range("J1").Value = "Yearly Change"
        Range("K1").Value = "Percent Change"
        Range("L1").Value = "Total Stock Volume"


        Rowprint = 1
        
        For i = 2 To Cells(Rows.Count, 1).End(xlUp).Row
            
            
            If Cells(i, 1).Value <> Cells(i - 1, 1).Value Then
                Rowprint = Rowprint + 1
                Cells(Rowprint, 9).Value = Cells(i, 1).Value
                OpenPrice = Cells(i, 3).Value
                Volume = 0
                OpenRow = i
                
            ElseIf Cells(i, 1).Value <> Cells(i + 1, 1).Value Then
                ClosingPrice = Cells(i, 6).Value

                If OpenPrice = 0 Or ClosingPrice = 0 Then
                    YearlyChange = 0
                    PercentChange = 0
                Else
                    YearlyChange = ClosingPrice - OpenPrice
                    PercentChange = (ClosingPrice - OpenPrice) / OpenPrice
                    Cells(Rowprint, 10).Value = YearlyChange
                    Cells(Rowprint, 11).Value = PercentChange
                    CloseRow = i
                    RowRange = "G" + Trim(Str(OpenRow)) + ":G" + Trim(Str(CloseRow))
                    Volume = Application.Sum(Range(RowRange))
                    Cells(Rowprint, 12).Value = Volume
                End If
                      
                    If YearlyChange > 0 Then
                        Cells(Rowprint, 10).Interior.ColorIndex = 4
                    Else
                        Cells(Rowprint, 10).Interior.ColorIndex = 3
                    End If
       
            End If
       
        Next i

        ActiveSheet.Columns(11).NumberFormat = "0.00%"
        
    Challenge
                
    Next ws
   
End Sub

Sub Challenge()
Dim i As Integer

        Range("P1").Value = "Ticker"
        Range("Q1").Value = "Value"
        Range("O2").Value = "Greatest Percent Increase"
        Range("O3").Value = "Greatest Percent Decrease"
        Range("O4").Value = "Greatest Total Volume"
        
        Range("Q2").Value = WorksheetFunction.Max(Range("K:K"))
        Range("Q3").Value = WorksheetFunction.Min(Range("K:K"))
        Range("Q4").Value = WorksheetFunction.Max(Range("L:L"))
        
        For i = 2 To Cells(Rows.Count, 9).End(xlUp).Row
            If Cells(i, 11) = Range("Q2").Value Then
            Range("P2").Value = Cells(i, 9)
            ElseIf Cells(i, 11) = Range("Q3").Value Then
            Range("P3").Value = Cells(i, 9)
            ElseIf Cells(i, 12) = Range("Q4").Value Then
            Range("P4").Value = Cells(i, 9)
            End If
            
        Next i
        
        ActiveSheet.Range("Q2:Q3").NumberFormat = "0.00%"
        

End Sub



