#sh
./jemdoc -c mysite.conf *.jemdoc

ls $DIR/*/ >/dev/null 2>&1

for file in `find . -mindepth 2 -name "compile.sh"`; do cd `dirname $file` && sh ./compile.sh && cd - ; done

# for file in `find . -name "*.pdf"`; do pdf2htmlEX --dest-dir `dirname $file` --fit-width 1024 $file; done
