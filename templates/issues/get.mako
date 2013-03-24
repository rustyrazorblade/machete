## -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>

<%block name="metatitle">${issue.name}</%block>

<%block name="content">
    <div class="container">
        <h1>${issue.name}</h1>

        <div>${issue.description}</div>
    </div>
</%block>
