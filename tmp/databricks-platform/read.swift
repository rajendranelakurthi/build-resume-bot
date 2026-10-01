import Foundation
import PDFKit
let d=PDFDocument(url:URL(fileURLWithPath:CommandLine.arguments[1]))!
print("Pages: \(d.pageCount)")
for i in 0..<d.pageCount {print(d.page(at:i)!.string ?? "")}
