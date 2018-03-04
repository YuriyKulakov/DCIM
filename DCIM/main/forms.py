from __future__ import unicode_literals

from django import forms

from utilities.forms import BootstrapMixin

OBJ_TYPE_CHOICES = (
    ('', 'All Objects'),
    ('Circuits', (
        ('provider', 'Providers'),
        ('circuit', 'Circuits'),
    )),
    ('DCIM', (
        ('site', 'Sites'),
        ('rack', 'Racks'),
        ('devicetype', 'Device types'),
        ('device', 'Devices'),
    )),
    ('IPAM', (
        ('vrf', 'VRFs'),
        ('aggregate', 'Aggregates'),
        ('prefix', 'Prefixes'),
        ('ipaddress', 'IP addresses'),
        ('vlan', 'VLANs'),
    )),
    ('Secrets', (
        ('secret', 'Secrets'),
    )),
    ('Tenancy', (
        ('tenant', 'Tenants'),
    )),
    ('Virtualization', (
        ('cluster', 'Clusters'),
        ('virtualmachine', 'Virtual machines'),
    )),
)


class SearchForm(BootstrapMixin, forms.Form):
    q = forms.CharField(
        label='Search'
    )
    obj_type = forms.ChoiceField(
        choices=OBJ_TYPE_CHOICES, required=False, label='Type'
    )
