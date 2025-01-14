LINKTERMINATION = """
{% if value %}
  {% if value.parent_object %}
    <a href="{{ value.parent_object.get_absolute_url }}">{{ value.parent_object }}</a>
    <i class="mdi mdi-chevron-right"></i>
  {% endif %}
  <a href="{{ value.get_absolute_url }}">{{ value }}</a>
{% endif %}
"""

CABLE_LENGTH = """
{% load helpers %}
{% if record.length %}{{ record.length|simplify_decimal }} {{ record.length_unit }}{% endif %}
"""

CABLE_TERMINATION_PARENT = """
{% if value.device %}
    <a href="{{ value.device.get_absolute_url }}">{{ value.device }}</a>
{% elif value.circuit %}
    <a href="{{ value.circuit.get_absolute_url }}">{{ value.circuit }}</a>
{% elif value.power_panel %}
    <a href="{{ value.power_panel.get_absolute_url }}">{{ value.power_panel }}</a>
{% endif %}
"""

DEVICE_LINK = """
<a href="{% url 'dcim:device' pk=record.pk %}">
    {{ record.name|default:'<span class="badge bg-info">Unnamed device</span>' }}
</a>
"""

DEVICEBAY_STATUS = """
{% if record.installed_device_id %}
    <span class="badge bg-{{ record.installed_device.get_status_class }}">
        {{ record.installed_device.get_status_display }}
    </span>
{% else %}
    <span class="badge bg-secondary">Vacant</span>
{% endif %}
"""

INTERFACE_IPADDRESSES = """
<div class="table-badge-group">
  {% for ip in record.ip_addresses.all %}
    {% if ip.status != 'active' %}
      <a href="{{ ip.get_absolute_url }}" class="table-badge badge bg-{{ ip.get_status_class }}" data-bs-toggle="tooltip" data-bs-placement="left" title="{{ ip.get_status_display }}">{{ ip }}</a>
    {% else %}
      <a href="{{ ip.get_absolute_url }}" class="table-badge">{{ ip }}</a>
    {% endif %}
  {% endfor %}
</div>
"""

INTERFACE_FHRPGROUPS = """
<div class="table-badge-group">
  {% for assignment in value.all %}
    <a href="{{ assignment.group.get_absolute_url }}">{{ assignment.group.get_protocol_display }}: {{ assignment.group.group_id }}</a>
  {% endfor %}
</div>
"""

INTERFACE_TAGGED_VLANS = """
{% if record.mode == 'tagged' %}
    {% for vlan in record.tagged_vlans.all %}
        <a href="{{ vlan.get_absolute_url }}">{{ vlan }}</a><br />
    {% endfor %}
{% elif record.mode == 'tagged-all' %}
  All
{% endif %}
"""

INTERFACE_WIRELESS_LANS = """
{% for wlan in record.wireless_lans.all %}
  <a href="{{ wlan.get_absolute_url }}">{{ wlan }}</a><br />
{% endfor %}
"""

POWERFEED_CABLE = """
<a href="{{ value.get_absolute_url }}">{{ value }}</a>
<a href="{% url 'dcim:powerfeed_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace">
    <i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i>
</a>
"""

POWERFEED_CABLETERMINATION = """
<a href="{{ value.parent_object.get_absolute_url }}">{{ value.parent_object }}</a>
<i class="mdi mdi-chevron-right"></i>
<a href="{{ value.get_absolute_url }}">{{ value }}</a>
"""

LOCATION_ELEVATIONS = """
<a href="{% url 'dcim:rack_elevation_list' %}?site={{ record.site.slug }}&location_id={{ record.pk }}" class="btn btn-sm btn-primary" title="View elevations">
    <i class="mdi mdi-server"></i>
</a>
"""

#
# Device component buttons
#

CONSOLEPORT_BUTTONS = """
{% if record.cable %}
    <a href="{% url 'dcim:consoleport_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace"><i class="mdi mdi-transit-connection-variant"></i></a>
    {% include 'dcim/inc/cable_toggle_buttons.html' with cable=record.cable %}
    {% if perms.dcim.delete_cable %}
        <a href="{% url 'dcim:cable_delete' pk=record.cable.pk %}?return_url={% url 'dcim:device_consoleports' pk=object.pk %}" title="Remove cable" class="btn btn-danger btn-sm">
            <i class="mdi mdi-ethernet-cable-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif perms.dcim.add_cable %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i></a>
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-lan-connect" aria-hidden="true"></i></a>
    <span class="dropdown">
        <button type="button" class="btn btn-success btn-sm dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="mdi mdi-ethernet-cable" aria-hidden="true"></span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="{% url 'dcim:consoleport_connect' termination_a_id=record.pk termination_b_type='console-server-port' %}?return_url={% url 'dcim:device_consoleports' pk=object.pk %}">Console Server Port</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:consoleport_connect' termination_a_id=record.pk termination_b_type='front-port' %}?return_url={% url 'dcim:device_consoleports' pk=object.pk %}">Front Port</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:consoleport_connect' termination_a_id=record.pk termination_b_type='rear-port' %}?return_url={% url 'dcim:device_consoleports' pk=object.pk %}">Rear Port</a></li>
        </ul>
    </span>
{% else %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-ethernet-cable" aria-hidden="true"></i></a>
{% endif %}
"""

CONSOLESERVERPORT_BUTTONS = """
{% if record.cable %}
    <a href="{% url 'dcim:consoleserverport_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace"><i class="mdi mdi-transit-connection-variant"></i></a>
    {% include 'dcim/inc/cable_toggle_buttons.html' with cable=record.cable %}
    {% if perms.dcim.delete_cable %}
        <a href="{% url 'dcim:cable_delete' pk=record.cable.pk %}?return_url={% url 'dcim:device_consoleserverports' pk=object.pk %}" title="Remove cable" class="btn btn-danger btn-sm">
            <i class="mdi mdi-ethernet-cable-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif perms.dcim.add_cable %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i></a>
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-lan-connect" aria-hidden="true"></i></a>
    <span class="dropdown">
        <button type="button" class="btn btn-success btn-sm dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="mdi mdi-ethernet-cable" aria-hidden="true"></span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="{% url 'dcim:consoleserverport_connect' termination_a_id=record.pk termination_b_type='console-port' %}?return_url={% url 'dcim:device_consoleserverports' pk=object.pk %}">Console Port</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:consoleserverport_connect' termination_a_id=record.pk termination_b_type='front-port' %}?return_url={% url 'dcim:device_consoleserverports' pk=object.pk %}">Front Port</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:consoleserverport_connect' termination_a_id=record.pk termination_b_type='rear-port' %}?return_url={% url 'dcim:device_consoleserverports' pk=object.pk %}">Rear Port</a></li>
        </ul>
    </span>
{% else %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-ethernet-cable" aria-hidden="true"></i></a>
{% endif %}
"""

POWERPORT_BUTTONS = """
{% if record.cable %}
    <a href="{% url 'dcim:powerport_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace"><i class="mdi mdi-transit-connection-variant"></i></a>
    {% include 'dcim/inc/cable_toggle_buttons.html' with cable=record.cable %}
    {% if perms.dcim.delete_cable %}
        <a href="{% url 'dcim:cable_delete' pk=record.cable.pk %}?return_url={% url 'dcim:device_powerports' pk=object.pk %}" title="Remove cable" class="btn btn-danger btn-sm">
            <i class="mdi mdi-ethernet-cable-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif perms.dcim.add_cable %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i></a>
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-lan-connect" aria-hidden="true"></i></a>
    <span class="dropdown">
        <button type="button" class="btn btn-success btn-sm dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="mdi mdi-ethernet-cable" aria-hidden="true"></span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="{% url 'dcim:powerport_connect' termination_a_id=record.pk termination_b_type='power-outlet' %}?return_url={% url 'dcim:device_powerports' pk=object.pk %}">Power Outlet</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:powerport_connect' termination_a_id=record.pk termination_b_type='power-feed' %}?return_url={% url 'dcim:device_powerports' pk=object.pk %}">Power Feed</a></li>
        </ul>
    </span>
{% else %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-ethernet-cable" aria-hidden="true"></i></a>
{% endif %}
"""

POWEROUTLET_BUTTONS = """
{% if record.cable %}
    <a href="{% url 'dcim:poweroutlet_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace"><i class="mdi mdi-transit-connection-variant"></i></a>
    {% include 'dcim/inc/cable_toggle_buttons.html' with cable=record.cable %}
    {% if perms.dcim.delete_cable %}
        <a href="{% url 'dcim:cable_delete' pk=record.cable.pk %}?return_url={% url 'dcim:device_poweroutlets' pk=object.pk %}" title="Remove cable" class="btn btn-danger btn-sm">
            <i class="mdi mdi-ethernet-cable-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif perms.dcim.add_cable %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i></a>
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-lan-connect" aria-hidden="true"></i></a>
    {% if not record.mark_connected %}
        <a href="{% url 'dcim:poweroutlet_connect' termination_a_id=record.pk termination_b_type='power-port' %}?return_url={% url 'dcim:device_poweroutlets' pk=object.pk %}" title="Connect" class="btn btn-success btn-sm">
            <i class="mdi mdi-ethernet-cable" aria-hidden="true"></i>
        </a>
    {% else %}
        <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-ethernet-cable" aria-hidden="true"></i></a>
    {% endif %}
{% endif %}
"""

INTERFACE_BUTTONS = """
{% if perms.ipam.add_ipaddress %}
    <a href="{% url 'ipam:ipaddress_add' %}?interface={{ record.pk }}&return_url={% url 'dcim:device_interfaces' pk=object.pk %}" class="btn btn-sm btn-success" title="Add IP address">
        <i class="mdi mdi-plus-thick" aria-hidden="true"></i>
    </a>
{% endif %}
{% if record.link %}
    <a href="{% url 'dcim:interface_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace"><i class="mdi mdi-transit-connection-variant"></i></a>
{% endif %}
{% if record.cable %}
    {% include 'dcim/inc/cable_toggle_buttons.html' with cable=record.cable %}
    {% if perms.dcim.delete_cable %}
        <a href="{% url 'dcim:cable_delete' pk=record.cable.pk %}?return_url={% url 'dcim:device_interfaces' pk=object.pk %}" title="Remove cable" class="btn btn-danger btn-sm">
            <i class="mdi mdi-ethernet-cable-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif record.wireless_link %}
    {% if perms.wireless.delete_wirelesslink %}
        <a href="{% url 'wireless:wirelesslink_delete' pk=record.wireless_link.pk %}?return_url={% url 'dcim:device_interfaces' pk=object.pk %}" title="Delete wireless link" class="btn btn-danger btn-sm">
            <i class="mdi mdi-wifi-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif record.is_wired and perms.dcim.add_cable %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i></a>
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-lan-connect" aria-hidden="true"></i></a>
    {% if not record.mark_connected %}
    <span class="dropdown">
        <button type="button" class="btn btn-success btn-sm dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="mdi mdi-ethernet-cable" aria-hidden="true"></span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
            <li><a class="dropdown-item" href="{% url 'dcim:interface_connect' termination_a_id=record.pk termination_b_type='interface' %}?return_url={% url 'dcim:device_interfaces' pk=object.pk %}">Interface</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:interface_connect' termination_a_id=record.pk termination_b_type='front-port' %}?return_url={% url 'dcim:device_interfaces' pk=object.pk %}">Front Port</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:interface_connect' termination_a_id=record.pk termination_b_type='rear-port' %}?return_url={% url 'dcim:device_interfaces' pk=object.pk %}">Rear Port</a></li>
            <li><a class="dropdown-item" href="{% url 'dcim:interface_connect' termination_a_id=record.pk termination_b_type='circuit-termination' %}?return_url={% url 'dcim:device_interfaces' pk=object.pk %}">Circuit Termination</a></li>
        </ul>
    </span>
    {% else %}
        <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-ethernet-cable" aria-hidden="true"></i></a>
    {% endif %}
{% elif record.is_wireless and perms.wireless.add_wirelesslink %}
    <a href="{% url 'wireless:wirelesslink_add' %}?site_a={{ record.device.site.pk }}&location_a={{ record.device.location.pk }}&device_a={{ record.device.pk }}&interface_a={{ record.pk }}&site_b={{ record.device.site.pk }}&location_b={{ record.device.location.pk }}" class="btn btn-success btn-sm">
        <span class="mdi mdi-wifi-plus" aria-hidden="true"></span>
    </a>
{% endif %}
"""

FRONTPORT_BUTTONS = """
{% if record.cable %}
    <a href="{% url 'dcim:frontport_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace"><i class="mdi mdi-transit-connection-variant"></i></a>
    {% include 'dcim/inc/cable_toggle_buttons.html' with cable=record.cable %}
    {% if perms.dcim.delete_cable %}
        <a href="{% url 'dcim:cable_delete' pk=record.cable.pk %}?return_url={% url 'dcim:device_frontports' pk=object.pk %}" title="Remove cable" class="btn btn-danger btn-sm">
            <i class="mdi mdi-ethernet-cable-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif perms.dcim.add_cable %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i></a>
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-lan-connect" aria-hidden="true"></i></a>
    {% if not record.mark_connected %}
        <span class="dropdown">
            <button type="button" class="btn btn-success btn-sm dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <span class="mdi mdi-ethernet-cable" aria-hidden="true"></span>
            </button>
            <ul class="dropdown-menu dropdown-menu-end">
                <li><a class="dropdown-item" href="{% url 'dcim:frontport_connect' termination_a_id=record.pk termination_b_type='interface' %}?return_url={% url 'dcim:device_frontports' pk=object.pk %}">Interface</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:frontport_connect' termination_a_id=record.pk termination_b_type='console-server-port' %}?return_url={% url 'dcim:device_frontports' pk=object.pk %}">Console Server Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:frontport_connect' termination_a_id=record.pk termination_b_type='console-port' %}?return_url={% url 'dcim:device_frontports' pk=object.pk %}">Console Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:frontport_connect' termination_a_id=record.pk termination_b_type='front-port' %}?return_url={% url 'dcim:device_frontports' pk=object.pk %}">Front Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:frontport_connect' termination_a_id=record.pk termination_b_type='rear-port' %}?return_url={% url 'dcim:device_frontports' pk=object.pk %}">Rear Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:frontport_connect' termination_a_id=record.pk termination_b_type='circuit-termination' %}?return_url={% url 'dcim:device_frontports' pk=object.pk %}">Circuit Termination</a></li>
            </ul>
        </span>
    {% else %}
        <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-ethernet-cable" aria-hidden="true"></i></a>
    {% endif %}
{% endif %}
"""

REARPORT_BUTTONS = """
{% if record.cable %}
    <a href="{% url 'dcim:rearport_trace' pk=record.pk %}" class="btn btn-primary btn-sm" title="Trace"><i class="mdi mdi-transit-connection-variant"></i></a>
    {% include 'dcim/inc/cable_toggle_buttons.html' with cable=record.cable %}
    {% if perms.dcim.delete_cable %}
        <a href="{% url 'dcim:cable_delete' pk=record.cable.pk %}?return_url={% url 'dcim:device_rearports' pk=object.pk %}" title="Remove cable" class="btn btn-danger btn-sm">
            <i class="mdi mdi-ethernet-cable-off" aria-hidden="true"></i>
        </a>
    {% endif %}
{% elif perms.dcim.add_cable %}
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-transit-connection-variant" aria-hidden="true"></i></a>
    <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-lan-connect" aria-hidden="true"></i></a>
    {% if not record.mark_connected %}
        <span class="dropdown">
            <button type="button" class="btn btn-success btn-sm dropdown-toggle" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <span class="mdi mdi-ethernet-cable" aria-hidden="true"></span>
            </button>
            <ul class="dropdown-menu dropdown-menu-end">
                <li><a class="dropdown-item" href="{% url 'dcim:rearport_connect' termination_a_id=record.pk termination_b_type='interface' %}?return_url={% url 'dcim:device_rearports' pk=object.pk %}">Interface</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:rearport_connect' termination_a_id=record.pk termination_b_type='console-server-port' %}?return_url={% url 'dcim:device_rearports' pk=object.pk %}">Console Server Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:rearport_connect' termination_a_id=record.pk termination_b_type='console-port' %}?return_url={% url 'dcim:device_rearports' pk=object.pk %}">Console Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:rearport_connect' termination_a_id=record.pk termination_b_type='front-port' %}?return_url={% url 'dcim:device_rearports' pk=object.pk %}">Front Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:rearport_connect' termination_a_id=record.pk termination_b_type='rear-port' %}?return_url={% url 'dcim:device_rearports' pk=object.pk %}">Rear Port</a></li>
                <li><a class="dropdown-item" href="{% url 'dcim:rearport_connect' termination_a_id=record.pk termination_b_type='circuit-termination' %}?return_url={% url 'dcim:device_rearports' pk=object.pk %}">Circuit Termination</a></li>
            </ul>
        </span>
    {% else %}
        <a href="#" class="btn btn-outline-dark btn-sm disabled"><i class="mdi mdi-ethernet-cable" aria-hidden="true"></i></a>
    {% endif %}
{% endif %}
"""

DEVICEBAY_BUTTONS = """
{% if perms.dcim.change_devicebay %}
    {% if record.installed_device %}
        <a href="{% url 'dcim:devicebay_depopulate' pk=record.pk %}?return_url={% url 'dcim:device_devicebays' pk=object.pk %}" class="btn btn-danger btn-sm">
            <i class="mdi mdi-minus-thick" aria-hidden="true" title="Remove device"></i>
        </a>
    {% else %}
        <a href="{% url 'dcim:devicebay_populate' pk=record.pk %}?return_url={% url 'dcim:device_devicebays' pk=object.pk %}" class="btn btn-success btn-sm">
            <i class="mdi mdi-plus-thick" aria-hidden="true" title="Install device"></i>
        </a>
    {% endif %}
{% endif %}
"""
