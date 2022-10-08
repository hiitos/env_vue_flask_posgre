provider "aws" {
    profile = "terraform"
    region = "ap-northeast-1"
}

resource "aws_instance" "hello-world" {
    ami = "ami-0218d08a1f9dac831"
    instance_type = "t2.micro"
    subnet_id = "subnet-00dcd4caf121aac0a"

    tags = {
        Name = "HelloWorld"
    }

}