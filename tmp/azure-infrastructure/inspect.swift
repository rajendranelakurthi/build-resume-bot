import AppKit
import PDFKit
let path=CommandLine.arguments[1]
let doc=PDFDocument(url:URL(fileURLWithPath:path))!
print("Pages: \(doc.pageCount)")
for i in 0..<doc.pageCount {
 let page=doc.page(at:i)!
 print("Page \(i+1): \((page.string ?? "").count) characters")
 let img=page.thumbnail(of:NSSize(width:900,height:1273),for:.mediaBox)
 let rep=NSBitmapImageRep(data:img.tiffRepresentation!)!
 try! rep.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"tmp/azure-infrastructure/page-\(i+1).png"))
}
