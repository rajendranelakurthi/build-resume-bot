import Foundation
import AppKit
import PDFKit
let source = CommandLine.arguments[1]
let output = CommandLine.arguments[2]
guard let doc = PDFDocument(url: URL(fileURLWithPath: source)) else { fatalError("Cannot open PDF") }
print("Pages: \(doc.pageCount)")
var text = ""
for i in 0..<doc.pageCount {
    let page = doc.page(at: i)!
    text += page.string ?? ""
    let bitmap = page.thumbnail(of: NSSize(width: 1200, height: 1700), for: .mediaBox)
    let rep = NSBitmapImageRep(data: bitmap.tiffRepresentation!)!
    try rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: "\(output)/page-\(i+1).png"))
}
try text.write(toFile: "\(output)/text.txt", atomically: true, encoding: .utf8)
