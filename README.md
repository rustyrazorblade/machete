Requirements-centric project and issue management experiment.


# REQUIREMENTS

You must have rexster installed with Titan.  You can use the included etc/rexster.xml.

Currently developing against rexster 2.2 but will upgrade asap.

```
npm install -g grunt-cli
```

# SETUP


```
wget https://s3-us-west-2.amazonaws.com/graphplatform.swmirror/titan.rexster-0.2.1.zip
unzip titan.rexster-0.2.1.zip

```

Move the unzipped directory to somewhere convenient.    Put the <titan-directory>/bin in your PATH.

```
export PATH=<titan-bin-dir>:$PATH
```

Within the machete directory, start titan in a detached screen:

```
screen -dm rexster.sh -s -c etc/rexster.xml
```

To stop titan:

```
rexster.sh -x
```

Download and start elastic search.  Instructions here:

`http://www.elasticsearch.org/guide/reference/setup/installation/`

I'm working on a Vagrant box to make this easier, but it's not even remotely close to ready.





