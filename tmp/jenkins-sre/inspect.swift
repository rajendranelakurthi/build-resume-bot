import AppKit
import PDFKit
let doc=PDFDocument(url:URL(fileURLWithPath:CommandLine.arguments[1]))!
print("Pages: \(doc.pageCount)")
for i in 0..<doc.pageCount {
 let p=doc.page(at:i)!
 print("Page \(i+1): \((p.string ?? "").count) characters")
 let img=p.thumbnail(of:NSSize(width:900,height:1273),for:.mediaBox)
 let rep=NSBitmapImageRep(data:img.tiffRepresentation!)!
 try! rep.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"tmp/jenkins-sre/page-\(i+1).png"))
}
