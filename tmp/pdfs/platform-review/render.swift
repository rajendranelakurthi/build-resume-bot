import Foundation
import AppKit
import PDFKit
let doc = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1]))!
let out = CommandLine.arguments[2]
print("Pages: \(doc.pageCount)")
var text = ""
for i in 0..<doc.pageCount {
 let page = doc.page(at: i)!
 text += page.string ?? ""
 let img = page.thumbnail(of: NSSize(width:1200,height:1700),for:.mediaBox)
 let rep = NSBitmapImageRep(data:img.tiffRepresentation!)!
 try rep.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"\(out)/page-\(i+1).png"))
}
try text.write(toFile:"\(out)/text.txt",atomically:true,encoding:.utf8)
