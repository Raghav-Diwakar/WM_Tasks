# Use minimal base image
FROM alpine:latest

# Install nginx
RUN apk --no-cache add nginx

# Add non-root user
RUN adduser -D -H -u 1001 webuser

# Create necessary directories
RUN mkdir -p \
    /var/www/localhost/htdocs \
    /etc/nginx/conf.d \
    /var/log/nginx \
    /run/nginx \
    /tmp/nginx_temp \
    /var/lib/nginx/logs  # Ensure the logs directory exists

# Copy static content and config
COPY index.html /var/www/localhost/htdocs/
COPY nginx.conf /etc/nginx/nginx.conf

# Ensure correct ownership and permissions for all required directories
RUN chown -R webuser:webuser /var/www /etc/nginx /var/log/nginx /run/nginx /tmp /var/lib/nginx /var/lib/nginx/logs && \
    chmod -R 755 /var/www /etc/nginx /var/log/nginx /run/nginx /tmp /var/lib/nginx /var/lib/nginx/logs

# Switch to non-root user
USER webuser

# Expose port 80
EXPOSE 80

# Run nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
