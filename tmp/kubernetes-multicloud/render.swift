import AppKit
import PDFKit
let d=PDFDocument(url:URL(fileURLWithPath:CommandLine.arguments[1]))!
print("Pages: \(d.pageCount)")
for i in 0..<d.pageCount {let p=d.page(at:i)!;let img=p.thumbnail(of:NSSize(width:900,height:1273),for:.mediaBox);let r=NSBitmapImageRep(data:img.tiffRepresentation!)!;try! r.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"tmp/kubernetes-multicloud/page-\(i+1).png"))}
