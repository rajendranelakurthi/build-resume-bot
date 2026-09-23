import Foundation
import PDFKit
import AppKit
let doc=PDFDocument(url:URL(fileURLWithPath:CommandLine.arguments[1]))!
print("Pages: \(doc.pageCount)")
for i in 0..<doc.pageCount {
 let p=doc.page(at:i)!
 print(p.string ?? "")
 let img=p.thumbnail(of:NSSize(width:900,height:1273),for:.mediaBox)
 let b=NSBitmapImageRep(data:img.tiffRepresentation!)!
 try b.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"tmp/aks-senior/page-\(i+1).png"))
}
