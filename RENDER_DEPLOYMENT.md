# Deploying Sepik Fresh to Render

## Prerequisites
1. Push your code to GitHub
2. Create a Render account at https://render.com

## Deployment Steps

### 1. Create Web Service
1. Go to Render Dashboard
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository: `https://github.com/DEVE123-dev/Sepik-Fresh-Order-Tracking-System-.git`
4. Configure the service:
   - **Name**: `sepik-fresh`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Environment**: `Python 3`
   - **Build Command**: `cd sepik_fresh && pip install -r requirements.txt`
   - **Start Command**: `cd sepik_fresh && gunicorn --config gunicorn_config.py wsgi:application`

### 2. Set Environment Variables
In the Render dashboard, add these environment variables:

```
FLASK_ENV=production
SECRET_KEY=<generate-a-random-secret-key>
DATABASE_PATH=sepik_fresh/database/sepik_fresh.db
```

To generate SECRET_KEY, run:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 3. Database Setup
**Option A: SQLite (Simple)**
- Your SQLite database will be included in the deployment
- **Note**: Data will reset on each deployment (Render's ephemeral filesystem)

**Option B: PostgreSQL (Recommended for Production)**
1. In Render Dashboard, create a PostgreSQL database
2. Update `config.py` to use PostgreSQL instead of SQLite
3. Install `psycopg2-binary` in requirements.txt
4. Link database to your web service

### 4. Deploy
1. Click **"Create Web Service"**
2. Render will automatically build and deploy
3. Your app will be live at: `https://sepik-fresh.onrender.com`

## Important Notes

### Free Tier Limitations
- App spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- SQLite data resets on each deployment

### For Production Use
1. Upgrade to paid plan ($7/month)
2. Use PostgreSQL database instead of SQLite
3. Set up persistent disk for file uploads
4. Configure custom domain

### Email Configuration
Update `email_utils.py` with production email settings:
- Use environment variables for email credentials
- Configure SMTP server (Gmail, SendGrid, etc.)

### Static Files
Static files are served automatically by Flask in production mode.

## Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Verify `requirements.txt` has all dependencies
- Ensure Python version compatibility

### App Crashes
- Check application logs in Render dashboard
- Verify environment variables are set correctly
- Check database connection settings

### Database Issues
- For SQLite: Data resets on deployment (use PostgreSQL for persistence)
- For PostgreSQL: Verify connection string is correct

## Monitoring
- View logs: Render Dashboard → Your Service → Logs
- Monitor performance: Render Dashboard → Metrics
- Set up alerts for downtime

## Updating Your App
1. Push changes to GitHub
2. Render automatically detects and redeploys
3. Or manually trigger deploy in Render dashboard

## Support
- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
