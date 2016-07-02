BASEDIR=$(CURDIR)

gh-pages:
	ghp-import -m "testing swagger UI instead of static swagger-codegen" -p $(BASEDIR)/swagger-ui/dist