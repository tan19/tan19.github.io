#sh
./jemdoc -c mysite.conf `find . -name "*.jemdoc"`
for file in `find . -name "*.pdf"`; do pdf2htmlEX --dest-dir `dirname $file` --fit-width 1100 $file; done