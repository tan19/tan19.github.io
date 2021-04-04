for /R "./Misc" %%f in (*.jemdoc) do echo @path && python jemdoc -c mysite.conf %%f
