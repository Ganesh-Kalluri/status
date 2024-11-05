# -*- coding: utf-8 -*-
#############################################################################
#
#    leewise Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY leewise Technologies(<https://www.leewise.com>)
#    Author: Ajith V(leewise@leewise.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': "Delivery Status on Sale Order",
    'summary': """Manage Delivery Status on Sale Order""",
    'description': "This module adds Delivery Status on Sale Order",
    'author': "leewise",
    'company': "leewise",
    'maintainer': 'leewise',

    'category': 'Sales',
    'version': '17.0.1.0.0',
    'depends': ['sale_stock', 'sale_management'],
    'data': ['views/sale_order.xml'],
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
