## -*- coding: utf-8 -*-
<!DOCTYPE html>
<html>
<head>
    <title><%block name="metatitle">Machete</%block></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <%block name="stylesheets">
        <!-- Bootstrap -->
        <link href="${url_for('static', filename='bootstrap/css/bootstrap.min.css')}" rel="stylesheet" media="screen">
    </%block>
</head>
<body>
    <%block name="topnav">
        <!-- top nav -->
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar navbar-inverse navbar-fixed-top">
                <div class="navbar-inner">
                    <div class="container-fluid">
                        <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="brand" href="#">Machete</a>
                        <div class="nav-collapse collapse">
                            <p class="navbar-text pull-right">
                                <!-- put username here -->
                            </p>
                            <ul class="nav">
                                <li><a href="/">Home</a></li>
                                <li class="active"><a href="/issues">Issues</a></li>
                                <li><a href="/questions">Questions</a></li>
                                <li><a href="/wiki">Wiki</a></li>
                            </ul>
                        </div><!--/.nav-collapse -->
                    </div>
                </div>
            </div>
        </div>
    </%block>
    <%block name="content"></%block>
    <%block name="footer"></%block>
    <%block name="scripts">
        <script src="http://code.jquery.com/jquery.js"></script>
        <script src="${url_for('static', filename='bootstrap/js/bootstrap.min.js')} "></script>
    </%block>
</body>
</html>