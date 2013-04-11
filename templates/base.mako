## -*- coding: utf-8 -*-
<!DOCTYPE html>
<html>
<head>
    <title><%block name="metatitle">Machete</%block></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
        }
    </style>

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
                        <a class="brand" href="/">Machete</a>
                        <div class="nav-collapse collapse">
                            <p class="navbar-text pull-right">
                                <!-- put username here -->
                            </p>
                            <ul class="nav">
                                <%
                                    def active_class(path):
                                        if request.path == path:
                                            return 'class="active"'
                                        return ''
                                %>
                                %if session.user:
                                <li ${active_class('/')}><a href="/">Home</a></li>
                                <li ${active_class('/issues/')}><a href="/issues">Issues</a></li>
                                <li ${active_class('/questions/')}><a href="/questions">Questions</a></li>
                                <li ${active_class('/wiki/')}><a href="/wiki">Wiki</a></li>

                                %else:
                                <li><a href="/login/">Login</a></li>
                                %endif
                            </ul>
                            %if session.user:
                            <ul class="nav pull-right">
                                <li><a href="/logout/">${session.user.email} Logout</a></li>
                            </ul>
                            %endif
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
        <script src="${url_for('static', filename='js/machete.js')}"></script>
    </%block>
</body>
</html>
