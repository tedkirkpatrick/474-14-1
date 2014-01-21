---
layout: course
title: Creating access keys for AWS REST calls
---

This tutorial shows you how to create an access key pair for AWS. You use
these keys to make REST calls from tools like boto.

<div class="well">The sequence of steps depends upon whether you are
creating keys for a root id or an IAM id. You only need to do this for one
kind of id.
</div>

## Creating access keys for an AWS root ID

* Sign on to your root ID. In the upper right corner of the console, there
is a menu that you can drop down from your name. Select the "Security
Credentials" item:<br/>
<img src="images/root-menu.png" class="img-responsive" alt="Root id console with menu expanded">

* On "Your Security Credentials", expand the "Access keys" item.
{% comment %}
:<br/>
<img src="images/root-security-credentials.png" class="img-responsive" alt="Security Credentials page (Unexpanded)">
{% endcomment %}
On the expanded item, press "Create New Access Key". Note that if you have
two active keys already created, you will not be able to create any
more. Delete one of your existing keys and you will be able to create a new
pair.<br/>
<img src="images/root-expanded-credentials-page.png" class="img-responsive" alt="Security Credentials page (Expanded)"><br/>


* At the bottom of the "Create Access Key" dialogue, you will see a button, "Download key file". Click it.<br/>
<img src="images/root-download-new-keys.png" class="img-responsive" alt="Download access key dialogue"><br/>
Pick a name for your file such as "access-keys.csv". Be sure to retain the .CSV filetype.

* Move your file to a secure directory and set its permissions so that only you can read it.

* **You're done!**

## Creating access keys for an IAM identifier

* Sign in to your IAM ID.Get the list of AWS services by clicking on the
  orange box in the upper left corner. Then select the IAM service:<br/>
<img src="images/iam-services-page.png" class="img-responsive" alt="AWS Service list">

* From the IAM page, select "Users":<br/>
<img src="images/iam-iam-page.png" class="img-responsive" alt="IAM page">

* On the Security Credentials page, select a user, go to the Security
  Credentials tab, and click on the "Manage Access Keys" button.<br/>
<img src="images/iam-security-credentials-page.png" class="img-responsive" alt="IAM user Security Credentials page">

* At the bottom of the "Manage Access Key" dialogue, you will see a button,
"Create Access Key". Click it.  Note that if you have two active keys
already created, you will not be able to create any more. Delete one of your
existing keys and you will be able to create a new pair.  <br/>
<img src="images/iam-create-key-page.png" class="img-responsive" alt="IAM Manage Access Keys dialogue">

* At the bottom of the "Manage Access Keys" dialogue, you will see a button, "Download Credentials". Click it.<br/>
<img src="images/iam-download-credentials-page.png" class="img-responsive" alt="Manage access keys dialogue"><br/>
Pick a name for your file such as "access-keys.csv". Be sure to retain the .CSV filetype.

* Move your file to a secure directory and set its permissions so that only you can read it.

* **You're done!**

