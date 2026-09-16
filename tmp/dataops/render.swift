import Foundation
import PDFKit
import AppKit
let doc=PDFDocument(url:URL(fileURLWithPath:CommandLine.arguments[1]))!
print("Pages: \(doc.pageCount)")
for i in 0..<doc.pageCount {
 let p=doc.page(at:i)!
 print(p.string ?? "")
 let im=p.thumbnail(of:NSSize(width:850,height:1200),for:.mediaBox)
 let data=NSBitmapImageRep(data:im.tiffRepresentation!)!.representation(using:.png,properties:[:])!
 try! data.write(to:URL(fileURLWithPath:"tmp/dataops/page-\(i+1).png"))
}
