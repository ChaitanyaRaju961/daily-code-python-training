#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install boto3')


# In[2]:


import boto3
s3=boto3.client("s3")


# In[5]:


bucket_name="samplebucket--143a0e60"
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint":"eu-north-1"}
)
print(f"Bucket '{bucket_name}' created successfully!")


# In[6]:


response=s3.list_buckets()
print("Existing Buckets:")
for bucket in response["Buckets"]:
    print(f"- {bucket['Name']}")


# s3.upload_file("test.text","samplebucket--143a0e60","data/testfile1.txt")
# print("Upload complete!")

# In[7]:


s3.download_file("test.text","samplebucket--143a0e60","data/testfile1.txt")
print("Download complete!")


# In[8]:


response=s3.list_objects_v2(Bucket="samplebucket--143a0e60")


# In[ ]:




