
.PHONY: setup

TARGET = transapi-frontend

setup:
	vue create $(TARGET)
	cp _files/App.vue $(TARGET)/src/
	cp _files/Translation.vue $(TARGET)/src/components/
	( cd $(TARGET) ; vue add electron-builder )
	./init-packages.py $(TARGET)
	( cd $(TARGET) ; npm install )

clean:
	find . -type f -name '*~' -exec rm {} \; -print
