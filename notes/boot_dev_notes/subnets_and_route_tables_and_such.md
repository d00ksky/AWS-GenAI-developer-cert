Subnets let's us divide VPC into smaller subnets that then go to Availability Zones

---

Each subnet is connected to an Availability Zone (AZ), which is one or more physical AWS data centers in a region. If we put our subnets in different AZs, a power outage affecting one AZ should not affect the other.

---

Then after we create subnets they are still not connected.
We need IGW Internet Gateway

An Internet Gateway (IGW) that can connect them to the internet
A route that tells servers in these subnets to use that IGW

After attaching IGW we need route that are named route tables.
This lets us create rules for things we care about like local traffic.
If we don't have specific rule for something we send it to the internet.

---

A private subnet is a subnet whose resources are not accessible from the internet directly, but can still have some internet connectivity.

We could use firewall but better approach is with many layers of security.
One good option for that is nat (network address translation) which lets us keep a subnet private but still allow outbound access when we need it.
