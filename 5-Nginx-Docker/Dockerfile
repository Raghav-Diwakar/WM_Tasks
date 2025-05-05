# Use minimal base image
FROM alpine:latest

# Install lighttpd
RUN apk --no-cache add lighttpd

# Add non-root user
RUN adduser -D -H -u 1001 webuser
# -D: Creates user without a password.
# -H: No home directory.

# Prepare web root
RUN mkdir -p /var/www/localhost/htdocs

# Copy content and config
COPY index.html /var/www/localhost/htdocs/
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf

# Set permissions
RUN chown -R webuser:webuser /var/www /etc/lighttpd /tmp

# Use non-root user
USER webuser

# Expose port
EXPOSE 80

# Run server in foreground
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
# -D: Runs in the foreground (important in containers).
# -f: Specifies the config file path.