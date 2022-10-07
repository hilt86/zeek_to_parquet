# zeek_to_parquet
Simple python script to convert Zeek ascii logs to parquet format and upload to Amazon S3

### Installation

Install dependencies

`pip install zat awscli fastparquet s3fs`

Add your credentials

`aws configure`

Edit `/opt/zeek/share/zeekctl/scripts/archive-log` script (let me know if there is a better way). I've placed this script just before archive-log deletes
the logfile.

```
158
159 # convert zeek logs to parquet and uploda to s3
160 /usr/bin/python3 /root/to_parquet.py $file_name $base_name s3://zeek.threatbear.co/
161
162 rm -f $file_name
```

NOTE : Make sure you put the trailing slash on the `s3://zeek.threatbear.co/` URL otherwise the script will fail.

IMPORTANT: Zeek package updates will overwrite `/opt/zeek/share/zeekctl/scripts/archive-log` so until we find another way of running zeek postprocessors YOU WILL NEED TO MAKE THE EDIT AFTER EACH UPDATE!!

Restart Zeek
`zeekctl restart`

### IAM Policy Example

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::zeek.threatbear.co/*"
        }
    ]
}
```


