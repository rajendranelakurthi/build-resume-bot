import Foundation
import PDFKit
import AppKit
let path = CommandLine.arguments[1]
let doc = PDFDocument(url: URL(fileURLWithPath: path))!
print("Pages: \(doc.pageCount)")
for i in 0..<doc.pageCount {
 let page=doc.page(at:i)!
 print("PAGE \(i+1): \(page.string ?? "")")
 let img=page.thumbnail(of:NSSize(width:900,height:1273),for:.mediaBox)
 let bitmap=NSBitmapImageRep(data:img.tiffRepresentation!)!
 try bitmap.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"tmp/aws-release/page-\(i+1).png"))
}
