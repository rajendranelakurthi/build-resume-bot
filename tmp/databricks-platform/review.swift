import Foundation
import PDFKit
import AppKit
let d=PDFDocument(url:URL(fileURLWithPath:CommandLine.arguments[1]))!
print("Pages: \(d.pageCount)")
for i in 0..<d.pageCount {
let p=d.page(at:i)!
print(p.string ?? "")
let img=p.thumbnail(of:NSSize(width:900,height:1273),for:.mediaBox)
let b=NSBitmapImageRep(data:img.tiffRepresentation!)!
try b.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"tmp/databricks-platform/page-\(i+1).png"))
}
