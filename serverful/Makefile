IMAGE_NAME_APP = "lpr"
IMAGE_TAG_APP = "v0.1.0"
TGZ_APP = "lpr.tgz"


deploy: package
	@echo "Deploy app ..."
	@scp $(TGZ_APP) aliyun-server:~/


package: build
	@echo "Package app ..."
	@docker save $(IMAGE_NAME_APP):$(IMAGE_TAG_APP) > $(TGZ_APP)


build:
	@echo "Build app..."
	@docker build -t $(IMAGE_NAME_APP):$(IMAGE_TAG_APP) .