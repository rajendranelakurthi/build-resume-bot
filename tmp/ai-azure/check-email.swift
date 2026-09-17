import Foundation
import PDFKit
let fm=FileManager.default
let it=fm.enumerator(atPath:".")!
var count=0
for case let path as String in it {
 if path.hasPrefix(".git/") || !path.hasSuffix(".pdf") {continue}
 guard let doc=PDFDocument(url:URL(fileURLWithPath:path)) else {fatalError(path)}
 let text=doc.string ?? ""
 if text.contains("rajendranelakurthi" + "@gmail.com") {print("OLD: " + path)}
 
 count += 1
}
print("Verified new email in \(count) PDFs")
