import sys
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE
from ldap3.core.exceptions import LDAPCursorError




server_name = "odin.kuben.it"
domain_name = "odin.kuben.it"
user_name = "simen"
password = "Q2w3e4r5"

"""
format_string = '{:25} {:>6} {:19} {:19} {}'
print(format_string.format('User', 'Logins', 'Last Login', 'Expires', 'Description'))
"""

server = Server(server_name, get_info=ALL)
conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM, auto_bind=True)
conn.search('dc=odin,dc=kuben,dc=it', '(GivenName=Alf)')

print(conn)

"""
domain = ADDomain('kuben.it')
ldap = domain.get_ldap_uris()
ldap2 = domain.get_ldap_servers()
# session = ADSession(ldap, domain)

# session = domain.create_session_as_user('simen@kuben.it', 'Q2w3e4r5')

# users = session.find_users_by_common_name("Simen", ["GivenName"])

print(domain)
print(ldap)
print(ldap2)"""